TEXT_TO_CHAT="""I will provide user_info and a job_description.
Your task is to generate a JSON format CV based on the provided information.
The CV should be tailored to pass ATS (Applicant Tracking Systems) by ensuring keywords and phrases from the job description are incorporated.
Keep the facts unchanged — such as the technologies used in the user’s experience.
Rephrase the information to make it more concise and readable, but maintain the core details.
The JSON should contain:
"summary": A brief professional overview.
"experience": Relevant roles and responsibilities. It should be a list of jsons of the form {"role": "ROLE_NAME", "responsibilities": ["RESPONSIBILITY1", "RESPONSIBILITY2"]}.
Education: Relevant degrees and coursework related to the job description. It should be a list of jsons of the form {"degree": "DEGREE_NAME", "details": "COURSEWORK"}.
Selected Projects: Projects that are most relevant to the job. It should be a list of jsons of the form {"project_name": "PROJECT_NAME", "details": "PROJECT_DETAILS"}.
"""


RESPONSE_JSON = {
    "name": "Michał Taczała",
    "header_basic_info": [
        "Warsaw/Lublin, Poland",
        "+48 727 777 060",
        "taczalamichal5@gmail.com",
        "https://www.linkedin.com/in/micha\%C5\%82-tacza\%C5\%82a-8aa13a244/",
        "https://github.com/MichalTaczala"
    ],
    "educations": [
        {
            "school_name": "Warsaw University of Technology",
            "faculty": "Faculty of Electronics and Information Technology",
            "degree": "BSc in Software Control and Robotics",
            "start_date": "2019-10-01",
            "end_date": "2023-06-30",
            "details": [
                "Relevant coursework: Algorithms and Data Structures, Object-Oriented Programming, Digital Signal Processing, Computer Vision",
                "GPA: 4.5/5.0",
            ],
        },
        {
            "school_name": "Warsaw University of Technology",
            "faculty": "Mathematics and Information Science",
            "degree": "MSc in Data Science",
            "start_date": "2023-10-01",
            "end_date": "2025-06-30",
            "details": [
                "Expected coursework: Machine Learning, Big Data Analytics, Deep Learning, Natural Language Processing",
                "Expected GPA: 4.5/5.0",
            ],
        },
        {
            "school_name": "Korea Advanced Institute of Science and Technology(KAIST)",
            "faculty": "Kim Jaechul School of AI",
            "degree": "Exchange AI MSc student",
            "start_date": "2024-08-25",
            "end_date": "2024-12-20",
        }
    ],
    "workExperience": [
        {
            "job_name": "Junior Software Developer",
            "company_name": "Sciamus",
            "start_date": "2022-05-01",
            "end_date": "2022-12-31",
            "details": [
                "Developed a Java mobile application for tracking personal finances",
                "Implemented a RESTful API using Django and Django REST framework",
                "Utilized SQLite for local data storage and Firebase for cloud storage",
            ]
        },
        {
            "job_name": "Software Developer",
            "company_name": "IT Touch",
            "start_date": "2023-01-01",
            "end_date": "2024-07-30",
            "details": [
                "Developed a Flutter mobile application for stock trading",
                "Integrated third-party APIs for real-time stock data and analytics",
            ]

        },
    ],
    "projects": [
        {
            "project_name": "Personal Finance Tracker",
            "details": [
                "Developed a Java mobile application for tracking personal finances",
                "Implemented a RESTful API using Django and Django REST framework",
                "Utilized SQLite for local data storage and Firebase for cloud storage",
            ]
        },
        {
            "project_name": "Stock Trading App",
            "details": [
                "Developed a Flutter mobile application for stock trading",
                "Integrated third-party APIs for real-time stock data and analytics",
            ]
        },
    ],
    "skills": [
        "Java",
        "Python",
        "Dart",
        "Flutter",
        "Django",
        "RESTful API",
        "SQLite",
        "Firebase",
        "Git",
        "Linux",
        "Data Structures",
        "Algorithms",
        "Object-Oriented Programming",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Big Data Analytics",
    ],
    "languages": [
        "English Advanced (C1)",
        "Polish Native",
        "Japanese Intermediate (N3)",
    ],
    "certifications": [
        "Google Cloud Associate Engineer - 06.2024",
        "Japanese Language Proficiency Test N3 - 06.2022",
        "Academic Proficiency in English C1 - 06.2024",
    ],
}

CURRENT_USER_DATA = {
    "educations": [
        {
            "degree": "BSc in Software Control and Robotics",        
            "start_date": "2019-10-01",
            "end_date": "2023-06-30",
            "details": "I achieved GPA of 4.5/5. I learned a lot on automation, robotics, and software development. I learned python for robotics, and artificial inteligence, because i took many extra courses on ML and AI. I attended the robotics student association where i was programming in python semi-autonomous rc car for competition where we achieved the third place. I learned git and data stuctures and algorithms as well. I also learned java for backend programming and SQL for relational databases. I learned flutter here creating a project for blind people. ",
        },
        {
            "degree": "MSc in Data Science",
            "start_date": "2023-10-01",
            "end_date": "2025-06-30",
            "details": "I am currently pursuing a MSc in Data Science. I am learning a lot about machine learning, deep learning, and big data analytics. I am also taking courses on natural language processing and computer vision. I am planning to specialize in data science and work on projects related to AI and ML. I learned technologies like apache stack(hadoop, kafka, pyspark), also ML libraries like numpy, pandas, pytorch. I worked a lot with python, and created many projects in this language. I build a few projects on google cloud platform where i was using many components like dataflow, app engine, and few others. I was also using terraform. I improve my language as this degree is in english. I also had the opportunity to collaborate with studens from other countries.",
        },
        {
            "degree": "Exchange AI MSc student",
            "start_date": "2024-08-25",
            "end_date": "2024-12-20",
            "details": "I was an exchange student in South Korea on the best university of technology in this country. I was studying AI and ML. I was learning a lot about korean culture. I was also working on projects with international students. I was using python and pytroch for many projects. I improved my language skills and gained a lot of knowledge on computer vision, nlp, and machine learning in general.",
        }
    ],
    "workExperience": [
        {
            "how_long": "8 months",
            "details": "I was working as a Junior Software Developer. I was developing a Java backend application for managing sim cards. I was responsible for adding new functionalities to the system, working with microservice architecture, configuring cloud, gitlab ci/cd pipelines, docker and writing tests in java including e2e tests and unit tests. I was using spring-boot on a daily basis. I was working with relational databases(postgres) and nosql(mongo). We had daily meetings with the clients, and we were working in agile. with 2 weeks sprints.",
        },
        {
            "how_long": "1 year and 7 months",
            "details": "I was mainly responsible for developing a mobile app in flutter. I was building a stock and crypto trading application for a startup client. I learned flutter with its common libraries like bloc, stripe, http, firebase. I was responsible for the whole app development process from the design to the deployment. I was working with 4 other mobile developers and we were working in agile.",

        },
    ],
    "projects": [
        {
            "project_name": "CV ATS Parser Django",
            "details": [
                "I created a Django web application that parses CVs and job descriptions to generate a JSON format CV tailored for ATS",
                "Used GCP for hosting and OpenAI API for natural language processing",
            ]
        },
        {
            "project_name": "Airbnb for Garages",
            "details": [
                "Developed a Flutter mobile application for renting out garages and parking spaces",
                "Hosted app on Google Cloud Platform using Firebase for authentication and Cloud SQL for data storage",
                "Implemented geolocation services and payment processing using Stripe API",
                "Backend developed in Python Flask"
            ]
        },
        {
            "project_name:": "Graph finding reaction direction",
            "details": [
                "Project was about finding the correct prediction of the reaction for the given dataset",
                "Used python, numpy, pytorch",
                "Used graph-related ml algorithms like graph neural networks or mlp",
            ]
        },
        {
            "project_name": "Big Data Analytics",
            "details": [
                "Hosted on Google Cloud platform",
                "Used apache tools: pyspark, kafka, nifi",
                "We had to merge 2 different data sources(weather data api and flight api) and make real time predictions regarding flight delays",
                "Code written in python, numpy, pytorch",
            ],
        },
        {
            "project_name": "Deep learning for image recognition/image generation",
            "details": [
                "Used pytorch, numpy, pandas",
                "Created a model for image recognition (CNN)",
                "Created a model for image generation(Difusion model)",
            ],
        },
        {
            "project_name": "NLP for retrieving important information from documents",
            "details": [
                "Used python for obtaining different information from the documents",
            ],
        },
        {
            "project_name": "Building a predictive model to identify customers who use the marketing offer",
            "details": [
                "Used python, numpy, pandas, pytorch",
                "Used many models for predicting if the customer will use the marketing offer",
                "Tested different solutions like SVM, NB, QDA, Random Forest",
                "Selected important features using Boruta algorithm",
            ]
        }
    ],
    "languages": [
        "English Advanced (C1)",
        "Polish Native",
        "Japanese Intermediate (N3)",
    ],
    "certifications": [
        "Academic Proficiency in English C1 - 06.2024",
        "Japanese Language Proficiency Test N3 - 06.2022",
        "GCP Cloud Associate Engineer - 06.2023",
    ],
    "hard_skills_to_choose_from": [
        "Java",
        "Python",
        "Spring Boot",
        "SQL",
        "MongoDB",
        "Docker",
        "Kubernetes",
        "GCP",
        "Dart",
        "Flutter",
        "Django",
        "RESTful API",
        "Firebase",
        "Git",
        "Linux",
        "Data Structures",
        "Algorithms",
        "Object-Oriented Programming",
        "Machine Learning",
        "Deep Learning",
        "Natural Language Processing",
        "Computer Vision",
        "Big Data Analytics",
        "HTTP Protocol",
        "Stripe API",
    ],
}