# NOMIS Tools

This repository is a little collection of tools and notes for working with Nomis and the Nomis API.

## API Reference

https://www.nomisweb.co.uk/api/v01/help

## List of datasets

https://www.nomisweb.co.uk/api/v01/dataset/def.htm

## Get a Codelist

```
python3 codelist.py NM_144_1 cell TEXT
python3 codelist.py NM_144_1 cell JSON
```

The first of these commands gives the following output; the second prints the
same information in JSON format.

```
0 All usual residents
1 Males
2 Females
3 Lives in a household
4 Lives in a communal establishment
5 Schoolchild or full-time student aged 4 and over at their non term-time address
6 Area (Hectares)
7 Density (number of persons per hectare)
```
