Oral Cancer Risk Analysis API
A dynamic Flask-based Web API designed for healthcare analytics, enabling real-time querying of patient demographics and risk factors from a 2GB SQLite database. Built for rapid prototyping and backend precision, this project demonstrates modular API design, secure database connectivity, and efficient data retrieval for clinical decision support.

Purpose & Functionality
This API empowers healthcare professionals and researchers to:
- Query patient demographics by age, gender, and name
- Analyze risk factors (alcohol intake, paan, smoking, tobacco chewing) across age groups
- Support resource planning through age-wise and gender-wise patient counts
- Ensure data integrity via secure adapter-based connection and runtime filtering

| **Category**                    | **Description**                                                                                                                                                                    |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Adapter Connection**          | Secure **SQLite3 adapter** with cursor-based execution for reliable query management and transaction handling.                                                                     |
| **Runtime GET Requests**        | Dynamic **RESTful endpoints** accepting user input via query parameters for real-time data filtering.                                                                              |
| **Risk Factor Analysis**        | Aggregates patients who answered **“No”** to specific habits (alcohol intake, paan, smoking, tobacco chewing).                                                                     |
| **Demographic Insights**        | Provides **age-wise and gender-wise patient counts** to support data-driven healthcare planning.                                                                                   |
| **Data Integrity**              | Ensures **database consistency and protection** using **parameterized SQL queries** to prevent injection vulnerabilities.                                                          |
| **Troubleshooting & Debugging** | Applied **debugging steps** such as verifying database connection strings, validating cursor objects, and testing adapter responses to maintain stable API–database communication. |



🧪 SQL Integration Highlights
This project uses embedded SQL queries within Python to:
Store & Retrieve: SELECT statements for patient data and schema introspection
Manipulate Data: Filtered queries for age and habit-based segmentation
Transaction Safety: Cursor-based execution ensures atomicity and rollback safety
Content Management: Structured JSON responses for frontend or analytics pipelines
Embedded SQL: Direct SQL statements within Flask routes for rapid prototyping

📁 API Endpoints
| Endpoint | Method | Description | 
| / | GET | Health check for API | 
| /schema | GET | View table schema | 
| /PatientNames?n=5 | GET | Get top N patient names | 
| /PatientNames_forAge?age=40 | GET | Filter patient names by age | 
| /patientcount_forAge?age=40 | GET | Count patients of a specific age | 
| /Agewisepatients | GET | Age-wise patient distribution | 
| /Genderwisepatients | GET | Gender-wise patient distribution | 
| /risk_factors | GET | Age-wise count of patients who answered "No" to habits | 

The project highlights originality in risk factor segmentation and demographic filtering

##Bottom-line of my SQL-driven backend application: I avoided using a global connection string as Each route establishes its own scoped database connection via get_db_connection(), ensuring thread safety, minimizing resource leaks, and preserving transactional integrity across concurrent requests. This design choice aligns with best practices for scalable, production-grade Flask APIs.
