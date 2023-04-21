## My_SQL_Projects

Hi - I will be uploading my SQL and Power BI new projects in this open source folder, so you can have a kick approach about part of my skills knowladge in these tools.

## Electronic Services

The next Power BI dashboard was developyed for a electronic technical service. The business utilizes an online software that collects information on their client repairs and provides real-time tracking updates on their status (such as entered, under diagnostic, repaired and ready for delivery, etc.).

The business not only provides services for individual customers (who typically visit the store), they also provide the same service to clients referred by insurance companies in the area. Therefore, the software was mainly designed to improve management and transparency for repairs coming from insurance companies, providing them with user access, written reports and equipments photos in a fast and efficient manner.

The following data was collected:

• Insurance company data (company ID and name)

• Repair data (repair ID, product type, repair creation date, and net profit from the repair)

• Tracking status and their respective update dates

Primary objectives --> evaluate delays in most requested repairs at the store, the trend of repair volumes for both individual and insurance-related repairs, and finally, analyze the profit trends historically.

Period of data --> 2019 (June-December), 2020 (January-December), and 2021 (January-March).

`Kindly note that all data referenced or presented has been modified to protect the confidentiality and integrity of the company's sensitive information.`

![Screenshot 2023-04-10 121402](https://user-images.githubusercontent.com/90732534/230930293-620ee2c6-d05b-4c36-8736-f3ec40519624.png)

![GIF](https://user-images.githubusercontent.com/90732534/230930352-26391ce5-56c4-422c-94b8-4b027d056e22.gif)

![GIF2](https://user-images.githubusercontent.com/90732534/230930708-e4fce111-0848-4505-9bbf-031a80ce7e9a.gif)

![GIF3](https://user-images.githubusercontent.com/90732534/230930723-293d48b0-8757-43e4-8d31-3fda7d19f218.gif)

## SQL queries used
```sql
# View with the repairs that were made (went through status 5: REPAIRED / TO BE DELIVERED)

CREATE VIEW Reparaciones_Status5 AS
(SELECT * FROM [dbo].[updateEstadosdeSeguimientos]
WHERE [tracking_status_id] = 5)

# View with the repairs that were delivered (went through status 7: DELIVERED)

CREATE VIEW Reparaciones_Status7 AS
(SELECT * FROM [dbo].[updateEstadosdeSeguimientos]
WHERE [tracking_status_id] = 7)

# View with the repairs that were charged, and went through states 5 and 7 in chronological order.

CREATE VIEW Reparaciones_cobradas AS
SELECT
T1.repair_id,
LEFT(T2.updated_at,10) as Fecha_Entregado
FROM [dbo].[Reparaciones_Status5] AS T1
INNER JOIN [dbo].[Reparaciones_Status7] AS T2 ON T1.repair_id =
T2.repair_id

# View with the intersection of Charged_repairs with Total_repairs, in order to obtain all 
# my relevant information for the Dashboard: Charged repair, repair profit (labor cost), 
# name of the repaired product, and the insurance company or individual it came from

CREATE VIEW reparaciones_full AS
SELECT
T1.id_reparacion,
pág. 12
T1.labor_cost,
LEFT(T1.created_at,10) as created_at,
T3.product_name,
T4.insure_name
FROM [dbo].[Reparaciones] as T1
INNER JOIN [dbo].[Reparaciones_cobradas] AS T2 ON T1.id_reparacion =
T2.repair_id
INNER JOIN [dbo].[Productos] AS T3 ON T1.product_id = T3.id_product
LEFT JOIN [dbo].[Companias] AS T4 ON T1.insurer_id = T4.id_company

```

## DER (Diagram Entity Relationship)
<img src="https://user-images.githubusercontent.com/90732534/230931925-e9c2a316-7734-49f2-a58c-f2517f57f285.png" width="65%">
<img src="https://user-images.githubusercontent.com/90732534/230932014-62fb18e6-d257-4feb-81ef-4a09ce9bf165.png" width="65%">
