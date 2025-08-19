Oral Cancer Risk Analysis API
A dynamic Flask-based Web API designed for healthcare analytics, enabling real-time querying of patient demographics and risk factors from a 2GB SQLite database. Built for rapid prototyping and backend precision, this project demonstrates modular API design, secure database connectivity, and efficient data retrieval for clinical decision support.

Purpose & Functionality
This API empowers healthcare professionals and researchers to:
- Query patient demographics by age, gender, and name
- Analyze risk factors (alcohol intake, paan, smoking, tobacco chewing) across age groups
- Support resource planning through age-wise and gender-wise patient counts
- Ensure data integrity via secure adapter-based connection and runtime filtering

Key Features
| Category | Description | 
| Adapter Connection | Secure SQLite3 adapter with cursor-based execution | 
| Runtime GET Requests | Dynamic endpoints accepting user input via query parameters | 
| Risk Factor Analysis | Filters patients who answered "No" to specific habits | 
| Demographic Insights | Age-wise and gender-wise patient counts for planning | 
| Data Integrity | Parameterized queries to prevent injection and ensure consistency | 



🧪 SQL Integration Highlights
This project uses embedded SQL queries within Python to:
- ✅ Store & Retrieve: SELECT statements for patient data and schema introspection
- ✅ Manipulate Data: Filtered queries for age and habit-based segmentation
- ✅ Transaction Safety: Cursor-based execution ensures atomicity and rollback safety
- ✅ Content Management: Structured JSON responses for frontend or analytics pipelines
- ✅ Embedded SQL: Direct SQL statements within Flask routes for rapid prototyping

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



Getting Started
- Clone the repository:
git clone https://github.com/your-username/oral-cancer-api.git
cd oral-cancer-api
- Ensure the SQLite database is placed at:
./oral_cancer_app/sqlite_backup/people.db
- Run the Flask server:
python app.py


The project highlights originality in risk factor segmentation and demographic filtering

##Bottom-line of my SQL-driven backend application: I avoided using a global connection string as Each route establishes its own scoped database connection via get_db_connection(), ensuring thread safety, minimizing resource leaks, and preserving transactional integrity across concurrent requests. This design choice aligns with best practices for scalable, production-grade Flask APIs.


Ready to archive this with pride. Let me know if you'd like a matching resume bullet or LinkedIn post to seal the deal.

