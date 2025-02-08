from __future__ import print_function
from cubes import Workspace, Cell, PointCut
import psycopg2

# 1. Create a workspace
workspace = Workspace()
workspace.register_default_store("sql", url="postgresql://postgres:2899@localhost:5432/cube_demandeservice")
workspace.import_model("testmodel.json")

# 2. Get a browser
browser = workspace.browser("fact_table_service_info")

# 3. Play with aggregates
result = browser.aggregate()

print("Total\n"
      "----------------------")

print("Record count : %8d" % result.summary["nombre_clients"])
print("Total amount : %8d" % result.summary["gains_total"])


#
# 4. Drill-down through a dimension
#

print("\n"
      "Drill Down by Category (top-level Item hierarchy)\n"
      "==================================================")
#
result = browser.aggregate(drilldown=["dim_temps"])
#print(list(result.drilldown))
for record in result:
    print(record)
#cube="fact_table_service_info"
#cut = cell.slice("dim_temps", 2019)
#cell = Cell(cube, cut)
#result = browser.aggregate(cell, drilldown=["dim_temps"])

#for row in result:
   # print("%s: %s" % (row["dim_temps.annees"], row["nombre_clients"]))
#cut = cubes.PointCut("dim_temps", [2019, 1])
#cell = cubes.Cell(cube, [cut])

#print(("%-20s%10s%10s%10s\n"+"-"*50) % ("Category", "Count", "Total", "Double"))
#
'''for row in result.table_rows("dm_temps"):
    print("%-20s%10d%10d%10d" % ( row.label, row.record["nbr_client"], row.record["gains"] )'''
