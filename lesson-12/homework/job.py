import requests
from bs4 import BeautifulSoup
import sqlite3
import csv
import argparse
from datetime import datetime

DB_NAME = "jobs.db"
BASE_URL = "https://realpython.github.io/fake-jobs/"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                company TEXT,
                location TEXT,
                description TEXT,
                apply_link TEXT,
                UNIQUE(title, company, location)
            )
        ''')

def get_jobs():
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
    except Exception as e:
        print(f"Error fetching jobs page: {e}")
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []
    for card in job_cards:
        title = card.find("h2", class_="title").text.strip()
        company = card.find("h3", class_="company").text.strip()
        location = card.find("p", class_="location").text.strip()
        apply_link = card.find_all("a")[1]["href"]
        apply_link = apply_link if apply_link.startswith("http") else BASE_URL + apply_link

        description = get_description(apply_link)
        jobs.append((title, company, location, description, apply_link))
    return jobs

def get_description(url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        desc_div = soup.find("div", class_="content")
        return desc_div.get_text(strip=True) if desc_div else "No description found."
    except:
        return "Error loading description."

def update_db(jobs):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        for job in jobs:
            cur.execute("SELECT description, apply_link FROM jobs WHERE title=? AND company=? AND location=?",
                        job[:3])
            result = cur.fetchone()

            if result is None:
                cur.execute("INSERT INTO jobs (title, company, location, description, apply_link) VALUES (?, ?, ?, ?, ?)", job)
                print(f"Inserted: {job[0]} at {job[1]}")
            elif result != job[3:]:
                cur.execute("UPDATE jobs SET description=?, apply_link=? WHERE title=? AND company=? AND location=?",
                            job[3:] + job[:3])
                print(f"Updated: {job[0]} at {job[1]}")

def filter_jobs(location=None, company=None):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        query = "SELECT title, company, location, description, apply_link FROM jobs WHERE 1=1"
        params = []
        if location:
            query += " AND location = ?"
            params.append(location)
        if company:
            query += " AND company = ?"
            params.append(company)
        cur.execute(query, params)
        return cur.fetchall()

def export_csv(jobs, filename=None):
    if not filename:
        now = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"filtered_jobs_{now}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Apply Link"])
        writer.writerows(jobs)
    print(f"Exported {len(jobs)} jobs to {filename}")

def main():
    parser = argparse.ArgumentParser(description="Fake Jobs Scraper")
    parser.add_argument("--location", help="Filter by job location")
    parser.add_argument("--company", help="Filter by company name")
    args = parser.parse_args()

    init_db()
    jobs = get_jobs()
    update_db(jobs)

    if args.location or args.company:
        filtered = filter_jobs(args.location, args.company)
        export_csv(filtered)

if __name__ == "__main__":
    main()
