#! /usr/bin/python

import csv
import re
from datetime import datetime

filename = 'Mathematics D-AMP Blog course review (Responses) - Form Responses 1.csv'
# filename = 'Course review.csv'

with open(filename, 'r') as f:
    reader = csv.reader(f)
    next(reader, None)
    # reader = csv.DictReader(f, delimiter=',')
    for r in reader:
        # print(r)
        if len(r[5]):
            tags = '\n - ' + '\n - '.join(re.split(';|,|\+', r[5]))
            tags = tags.lower()
        else:
            tags = ''

        # get date in req format
        date = datetime.strptime(r[0], '%m/%d/%Y %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
        r[2] = r[2].replace(' ','').upper() # course code
        r = [col.strip() for col in r] # remove trailing spaces
        # filename of file to be created
        md_file = f"_posts/{date.split()[0]}-{r[2].lower()}-{r[1].lower().replace(' ', '-')}.markdown"
        md = f'''---
layout: post
title:  "{r[2]}: {r[3]}"
date:   {date} +0530
categories: {re.split(';|,', r[5])[0].lower()}
tags:{tags}
author:
  name: "{r[1]}"
---

- Instructor: {r[6]}

- Pre-requisites: {r[4]}

- Semester in which the course was taken: {r[7]}

- Motivation for taking the course: {r[8]}

- Course Content: {r[9]}

- Lecture Quality and Pacing: {r[10]}

- Exams and Assignments: {r[11]}

- Grading Policy: {r[12]}

- Study Material and References: {r[13]}

- Follow-up Courses: {r[14]}

- Advice on Studying this course: {r[15]}
'''
        # print(md)
        # print(md_file)
        with open(md_file, 'w') as md_f:
            md_f.write(md)
