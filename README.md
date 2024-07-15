# ⚽ Fantasy Premier League Data Warehouse


> This project creates a robust data warehouse for Fantasy Premier League data, leveraging modern data engineering tools and techniques. Whether you want to generate insightful reports or build predictive models, this project has you covered.

![ETL Process](/Images/ETL%20Process.jpg)
### 🛠️ Technologies & Tools Used
**Apache Spark**, **Mage**, **PostgreSQL**, **Data Warehousing**, **Data Modeling**, **ETL**

## 📈 Project Stages

### 1. 🛠️ Environment Setup
Using **Docker** to create a consistent and reproducible development environment to run Spark, Mage, and PostgreSQL.

### 2. 🗂️ Data Modeling
Designing and implementing the Data Warehouse model in PostgreSQL to store and manage processed FPL data.

![Data Modeling](/Images/Data_Model.png)

### 3. 🔄 ETL Pipeline
Building the ETL pipeline using **Apache Spark** and orchestrating it with **Mage** to extract, transform, and load FPL data.

![ETL Pipeline](./Images/The%20pipline.jpeg)

### 4. 🧩 Workflow Orchestration
* Utilizing **Mage** to orchestrate and manage the data workflows.
* Setting **Triggers** to automate the ETL pipeline runs each gameweek.

![Triggers](./Images/testing%20the%20pipeline.jpeg)

---

## 🚀 Future Work

With this data warehouse, future enhancements can include:


- **⚽ Match Data Analysis**: Use match data to provide detailed statistics for each match.

- **📈 Team Performance Dashboard**: Develop features for fpl users to see their teams' performance statistics and insights.

- **📊 Generate Reports**: Integrate with Power BI or Tableau to create insightful visualizations.
- **🤖 Build Predictive Models**: Develop machine learning models to forecast player performance for upcoming gameweeks.

---

## 💻 Run the Project & Make Your Own Environment

You can set up your own environment by running:
```bash
git clone https://github.com/yourusername/fpl-data-warehouse.git
cd fpl-data-warehouse
docker-compose up -d
```
---
## 🤝 Join Me
I'm excited to make this an excellent resource for FPL enthusiasts and data analysts. If you have suggestions or want to contribute, please open an issue or submit a pull request. Let's collaborate to enhance this project!
