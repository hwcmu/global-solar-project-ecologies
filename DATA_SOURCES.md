# Data Sources

The source datasets are not redistributed in this repository. Download them from their publishers and retain their original licensing and attribution information.

## Global Solar Power Tracker

- Publisher: Global Energy Monitor
- Release used: February 2026
- Source: https://globalenergymonitor.org/projects/global-solar-power-tracker/
- Expected path: `data/Global-Solar-Power-Tracker-February-2026.xlsx`

The notebooks use phase-level utility-scale solar records and derive the retained size-status analysis tables from this workbook.

## Natural Earth Country Boundaries

- Dataset: Admin 0 - Countries, 1:110m cultural vectors
- Source: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/110m-admin-0-countries/
- Expected path: `data/natural_earth/ne_110m_admin_0_countries/ne_110m_admin_0_countries.shp`

Keep all shapefile sidecar files (`.dbf`, `.prj`, `.shx`, and related files) in the same directory.

## Directory Check

Before running the pipeline, the relevant part of the repository should look like:

```text
data/
├── Global-Solar-Power-Tracker-February-2026.xlsx
└── natural_earth/
    └── ne_110m_admin_0_countries/
        ├── ne_110m_admin_0_countries.shp
        ├── ne_110m_admin_0_countries.dbf
        ├── ne_110m_admin_0_countries.prj
        └── ne_110m_admin_0_countries.shx
```

