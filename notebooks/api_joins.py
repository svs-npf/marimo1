import marimo

__generated_with = "0.23.16"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import polars as pl 
    import duckdb as ddb 
    import httpx 
    import io 

    return ddb, httpx, io, mo, pl


@app.cell(hide_code=True)
def _(ddb, httpx, io, pl):
    def get_an():
        res = httpx.get("https://canadabuys.canada.ca/opendata/pub/awardNoticeComplete-avisAttributionComplet.csv",
             headers={"User-Agent":"Mozilla/5.0"})
        df = pl.read_csv(io.BytesIO(res.content))
        cols = [
          "title-titre-eng",
          "referenceNumber-numeroReference",
          "amendmentNumber-numeroModification",
          "solicitationNumber-numeroSollicitation",
          "contractNumber-numeroContrat",
          "publicationDate-datePublication",
          "contractAwardDate-dateAttributionContrat",
          "amendmentDate-dateModification",
          "contractStartDate-contratDateDebut",
          "contractEndDate-dateFinContrat",
          "contractAmount-montantContrat",
          "totalContractValue-valeurTotaleContrat",
          "contractCurrency-contratMonnaie",
          "awardStatus-attributionStatut-eng",

          "instrumentType-typeInstrument-eng",

          "amendmentType-typeModification-eng",

          "gsin-nibs",
          "gsinDescription-nibsDescription-eng",

          "unspsc",
          "unspscDescription-eng",

          "procurementCategory-categorieApprovisionnement",
          "noticeType-avisType-eng",

          "procurementMethod-methodeApprovisionnement-eng",

          "selectionCriteria-criteresSelection-eng",

          "limitedTenderingReason-raisonAppelOffresLimite-eng",

          "tradeAgreements-accordsCommerciaux-eng",

          "regionsOfDelivery-regionsLivraison-eng",

          "supplierLegalName-nomLegalFournisseur-eng",
          "contractingEntityName-nomEntitContractante-eng",   
          "endUserEntitiesName-nomEntitesUtilisateurFinal-eng",
   
          "awardDescription-descriptionAttribution-eng",
        ]
        df1 = df[cols]
        df2 = df2 = df1.rename(lambda c: c.split("-")[0].lower())
        rcmp_an = ddb.sql("SELECT * FROM df2 WHERE procurementcategory ILIKE '%GD%' AND contractingentityname ILIKE '%RCMP%'").pl()
        return rcmp_an


    return (get_an,)


@app.cell(hide_code=True)
def _(ddb, httpx, io, pl):
    def get_tn():
        res = httpx.get(
            "https://canadabuys.canada.ca/opendata/pub/tenderNoticeComplete-avisAppelOffresComplet.csv",
            headers={"User-Agent": "Mozilla/5.0"},
        )

        df = pl.read_csv(io.BytesIO(res.content))
        cols = [
            "title-titre-eng",
            "referenceNumber-numeroReference",
            "amendmentNumber-numeroModification",
            "solicitationNumber-numeroSollicitation",
            "publicationDate-datePublication",
            "tenderStatus-appelOffresStatut-eng",
            "tenderClosingDate-appelOffresDateCloture",
            "amendmentDate-dateModification",
            "expectedContractStartDate-dateDebutContratPrevue",
            "expectedContractEndDate-dateFinContratPrevue",
            "gsin-nibs",
            "gsinDescription-nibsDescription-eng",
            "unspsc",
            "unspscDescription-eng",
            "procurementCategory-categorieApprovisionnement",
            "noticeType-avisType-eng",
            "procurementMethod-methodeApprovisionnement-eng",
            "selectionCriteria-criteresSelection-eng",
            "limitedTenderingReason-raisonAppelOffresLimite-eng",
            "tradeAgreements-accordsCommerciaux-eng",
            "regionsOfOpportunity-regionAppelOffres-eng",
            "regionsOfDelivery-regionsLivraison-eng",
            "contractingEntityName-nomEntitContractante-eng",
            "endUserEntitiesName-nomEntitesUtilisateurFinal-eng",
            "contactInfoName-informationsContactNom",
            "noticeURL-URLavis-eng",
            "attachment-piecesJointes-eng",
            "tenderDescription-descriptionAppelOffres-eng",
        ]
        df1 = df[cols]
        df2 = df1.rename(lambda c: c.split("-")[0].lower())
        rcmp_tn = ddb.sql(
            "SELECT * FROM df2 WHERE procurementcategory ILIKE '%GD%' AND contractingentityname ILIKE '%RCMP%'"
        ).pl()
        return rcmp_tn

    return (get_tn,)


@app.cell(hide_code=True)
def _(ddb, httpx, io, pl):
    def get_ch():
        res = httpx.get(
            "https://canadabuys.canada.ca/opendata/pub/contractHistoryComplete-contratsOctroyesComplet.csv",
            headers={"User-Agent": "Mozilla/5.0"})

        df = pl.read_csv(io.BytesIO(res.content), infer_schema=False)
        cols = [
          "title-titre-eng",
  
  
          "amendmentNumber-numeroModification",
          "procurementNumber-numeroApprovisionnement",
          "solicitationNumber-numeroSollicitation",
          "contractNumber-numeroContrat",
          "numberOfRecords-nombreEnregistrements",
          "publicationDate-datePublication",
          "contractAwardDate-dateAttributionContrat",
          "amendmentDate-dateModification",
          "contractStartDate-contratDateDebut",
          "contractEndDate-dateFinContrat",
          "contractAmount-montantContrat",
          "totalContractValue-valeurTotaleContrat",
          "contractCurrency-contratMonnaie",
          "contractStatus-statutContrat-eng",
  
          "instrumentType-typeInstrument-eng",
  
          "amendmentType-typeModification-eng",
  
          "gsin-nibs",
          "gsinDescription-nibsDescription-eng",
  
          "unspsc",
          "unspscDescription-eng",
  
          "procurementCategory-categorieApprovisionnement",
          "noticeType-avisType-eng",

          "procurementMethod-methodeApprovisionnement-eng",

          "selectionCriteria-criteresSelection-eng",

          "limitedTenderingReason-raisonAppelOffresLimite-eng",

          "tradeAgreements-accordsCommerciaux-eng",

          "regionsOfDelivery-regionsLivraison-eng",

          "supplierLegalName-nomLegalFournisseur-eng",


          "supplierOperatingName-nomCommercialFournisseur-eng",

          "supplierEmployeeCount-fournisseurNombreEmployes-eng",





          "contractingEntityName-nomEntitContractante-eng",

          "endUserEntitiesName-nomEntitesUtilisateurFinal-eng",

          "endUserEntitiesOfficeName-bureauNomEntitesUtilisateurFinal-eng",

          "contactInfoName-informationsContactNom",

          "percentageOfGoodsByCountry-pourcentageDeBiensParPays",
          "tenderDescription-descriptionAppelOffres-eng",

        ]
        df1 = df[cols]
        df2 = df1.rename(lambda c: c.split("-")[0].lower())
        rcmp_ch = ddb.sql(
            "SELECT * FROM df2 WHERE procurementcategory ILIKE '%GD%'" # AND contractingentityname ILIKE '%RCMP%'"
        ).pl()
        return rcmp_ch


    return (get_ch,)


@app.cell
def _(get_an, get_ch, get_tn):
    rcmp_an = get_an()
    rcmp_tn = get_tn()
    rcmp_ch = get_ch()
    return rcmp_an, rcmp_ch, rcmp_tn


@app.cell
def _(rcmp_an, rcmp_ch, rcmp_tn):
    import pandas as pd
    from collections import defaultdict

    # Replace these with your actual DataFrames:
    tn = rcmp_tn.to_pandas() 
    an = rcmp_an.to_pandas()
    ch = rcmp_ch.to_pandas()

    # Convert column names to sets
    cols1 = set(tn.columns)
    cols2 = set(an.columns)
    cols3 = set(ch.columns)

    # Columns present in all three DataFrames
    overlap_all_three = cols1 & cols2 & cols3

    # Columns exclusive to each DataFrame
    exclusive_to_tn = cols1 - cols2 - cols3
    exclusive_to_an = cols2 - cols1 - cols3
    exclusive_to_ch = cols3 - cols1 - cols2

    # Columns shared by exactly two DataFrames
    shared_tn_an = (cols1 & cols2) - cols3
    shared_tn_ch = (cols1 & cols3) - cols2
    shared_an_ch = (cols2 & cols3) - cols1
    """
    # Print the results
    print("Columns present in all three DataFrames:")
    print(sorted(overlap_all_three))

    print("\nColumns exclusive to tn:")
    print(sorted(exclusive_to_tn))

    print("\nColumns exclusive to an:")
    print(sorted(exclusive_to_an))

    print("\nColumns exclusive to ch:")
    print(sorted(exclusive_to_ch))

    print("\nColumns shared by tn and an only:")
    print(sorted(shared_tn_an))

    print("\nColumns shared by tn and ch only:")
    print(sorted(shared_tn_ch))

    print("\nColumns shared by an and ch only:")
    print(sorted(shared_an_ch))
    """
    # Create a complete column comparison table
    all_columns = sorted(cols1 | cols2 | cols3)

    comparison = pd.DataFrame({
        "column": all_columns,
        "tn": [column in cols1 for column in all_columns],
        "an": [column in cols2 for column in all_columns],
        "ch": [column in cols3 for column in all_columns],
    })

    # Add a column describing where each column appears
    def get_location(row):
        locations = []

        if row["tn"]:
            locations.append("tn")
        if row["an"]:
            locations.append("an")
        if row["ch"]:
            locations.append("ch")

        return ", ".join(locations)

    comparison["dataframes"] = comparison.apply(get_location, axis=1)

    # Add a category for each column
    def get_category(row):
        if row["tn"] and row["an"] and row["ch"]:
            return "overlap_all_three"
        elif row["tn"] and not row["an"] and not row["ch"]:
            return "exclusive_to_tn"
        elif row["an"] and not row["tn"] and not row["ch"]:
            return "exclusive_to_an"
        elif row["ch"] and not row["tn"] and not row["an"]:
            return "exclusive_to_ch"
        elif row["tn"] and row["an"] and not row["ch"]:
            return "shared_tn_an_only"
        elif row["tn"] and row["ch"] and not row["an"]:
            return "shared_tn_ch_only"
        elif row["an"] and row["ch"] and not row["tn"]:
            return "shared_an_ch_only"

        return "unknown"

    comparison["category"] = comparison.apply(get_category, axis=1)

    # Display the comparison table
    print("\nComplete column comparison:")
    print(comparison.to_string(index=False))

    # Optional: save the comparison to a CSV file
    # comparison.to_csv("dataframe_column_comparison.csv", index=False)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Data Sets :
    1. Tender Notices
    2. Award Notices
    3. Contract History
    4. Standing Offers and Supply Arrangements
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    1. publicationDate: The date a tender notice, award notice, or contract is publicly published. (Used in the CanadaBuys tender notices, award notices, and contract history data files.)
        I see some tender start date thats earlier than publicationDate - "CanadaBuys :  procurement information feeding the platform comes from multiple systems and may not be immediately visible in the open-data files."
    2. tender_closing_date : Deadline for bids
    3. tender_status == "Open" means its open for bidding.
    4. amdendmentDate from tender dataset is different from the amendmentdate from award dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    if tn.tenderstatus is cancelled:
        tender is cancelled
    elif tn.tenderstatus is expired:
        if an.contractnumber is not null
            if an.awardstatus is active
                contract is active (someone got the contract)
            else (an.awardstatus is expired)
                contract is expired (Someone got the contract but it now expired)
        else tender is open
    else (tn.tenderstatus is open)







    2.
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(rcmp_tn):
    rcmp_tn.columns
    return


@app.cell(hide_code=True)
def _(mo, rcmp_tn):
    stage_1 = mo.sql(
        f"""
        SELECT
            rcmp_tn.solicitationnumber,
            rcmp_tn.title,
            rcmp_tn.unspscdescription AS unspsc_desc,
            rcmp_tn.tenderstatus AS tender_status,
            rcmp_tn.noticetype,
            rcmp_tn.amendmentnumber AS tender_amendment,
            rcmp_tn.amendmentdate AS amendment_date,
            rcmp_tn.publicationdate AS tender_pub_date,
            rcmp_tn.tenderclosingdate AS tender_closing_date,
            rcmp_tn.expectedcontractstartdate,
            rcmp_tn.expectedcontractenddate,
            rcmp_tn.attachment,
            rcmp_tn.tenderdescription,
            rcmp_tn.unspsc
    
    
    
        FROM
            rcmp_tn
            -- LEFT JOIN rcmp_an ON rcmp_an.solicitationnumber = rcmp_tn.solicitationnumber
            -- RIGHT JOIN valid_sno ON rcmp_tn.solicitationnumber = valid_sno.solicitationnumber
        WHERE
            rcmp_tn.publicationdate >= '2025-01-01'
            -- AND rcmp_tn.tenderclosingdate >= '2026-03-01'
            -- AND rcmp_an.solicitationnumber IS NULL -- Stage one only ?
          AND (
            EXISTS (
                SELECT
                    1
                FROM
                    UNNEST(
                        string_split(
                            REPLACE(COALESCE(rcmp_tn.unspsc, ''), '\n', ''),
                            '*'
                        )
                    ) AS code (unspsc_code)
                WHERE
                    TRIM(unspsc_code) IN (
                        '46151503',
                        '46171626',
                        '46151700',
                        '53102500',
                        '46220000',
                        '53102504',
                        '25101600',
                        '25101801',
                        '24100000',
                        '53100000',
                        '49200000',
                        '45121500',
                        '46182500',
                        '53102703',
                        '25101611',
                        '46101601',
                        '43190000',
                        '46171615',
                        '55121804',
                        '56101520',
                        '25174800',
                        '39112100',
                        '21101701',
                        '25132100',
                        '46100000'
                    )
    
            )
            OR rcmp_tn.title ILIKE '%rfp%' OR rcmp_tn.title ILIKE '%rfi%' )
        """,
        output=False
    )
    return (stage_1,)


@app.cell
def _(mo, stage_1):
    tender_table = mo.ui.table(
    stage_1,
    pagination=True,
    page_size=25,
    selection=None,
    show_column_summaries=False,
    show_data_types=True,
    show_download=True,
    show_search=True,
    max_columns=None,
    freeze_columns_left=["solicitationnumber", "title",],
    wrapped_columns=["title"], # , "attachment"],
    column_widths={
        "title": 200,
        "tenderdescription": 460,
        "attachment": 320,
    },
    label=f"Tender notices",
    max_height=650,
    )
    mo.vstack([mo.md("## 1. Tender notices"), tender_table])
   
    return


@app.cell(hide_code=True)
def _(mo, stage_1):
    stage_1_agg = mo.sql(
        f"""
        SELECT 
        	noticetype as notice_type, 
        	COUNT(noticetype) as counter, 
        FROM stage_1 
        GROUP BY noticetype
        """
    )
    return


@app.cell
def _(mo, rcmp_an, stage_1):
    stage_2 = mo.sql(
        f"""
        SELECT
            rcmp_an.solicitationnumber,
            CASE 
            	WHEN stage_1.solicitationnumber IS NOT NULL 
            	THEN 'Yes'
            	ELSE 'No'
            END AS exists_in_stage_1, 
            rcmp_an.title,
        	rcmp_an.awardstatus AS award_status,
            rcmp_an.noticetype,
            rcmp_an.amendmentnumber AS tender_amendment,
            rcmp_an.publicationdate AS award_pub_date,
            rcmp_an.amendmenttype,
            rcmp_an.amendmentdate, 
            rcmp_an.amendmentnumber,
    
            rcmp_an.totalcontractvalue, 
            rcmp_an.contractamount, 
            rcmp_an.contractawarddate,
            rcmp_an.contractstartdate,
          	rcmp_an.contractenddate,
          	rcmp_an.contractnumber,
            rcmp_an.awarddescription,
            rcmp_an.unspscdescription AS unspsc_desc,
            rcmp_an.supplierlegalname
    
        FROM
            rcmp_an
        	LEFT JOIN stage_1 ON stage_1.solicitationnumber = rcmp_an.solicitationnumber
            -- LEFT JOIN rcmp_ch ON rcmp_ch.solicitationnumber = rcmp_an.solicitationnumber
        WHERE
            rcmp_an.publicationdate >= '2025-01-01'
            -- AND rcmp_an.tenderclosingdate >= '2026-03-01'
            AND rcmp_an.solicitationnumber IS NOT NULL
            -- AND rcmp_ch.solicitationnumber IS NULL -- Stage two only
            AND( EXISTS (
                SELECT
                    1
                FROM
                    UNNEST(
                        string_split(
                            REPLACE(COALESCE(rcmp_an.unspsc, ''), '\n', ''),
                            '*'
                        )
                    ) AS code (unspsc_code)
                WHERE
                    TRIM(unspsc_code) IN (
                        '46151503',
                        '46171626',
                        '46151700',
                        '53102500',
                        '46220000',
                        '53102504',
                        '25101600',
                        '25101801',
                        '24100000',
                        '53100000',
                        '49200000',
                        '45121500',
                        '46182500',
                        '53102703',
                        '25101611',
                        '46101601',
                        '43190000',
                        '46171615',
                        '55121804',
                        '56101520',
                        '25174800',
                        '39112100',
                        '21101701',
                        '25132100',
                        '46100000'
                    )
            )  OR rcmp_an.title ILIKE '%rfp%' OR rcmp_an.title ILIKE '%rfi%' )
        """,
        output=False
    )
    return (stage_2,)


@app.cell
def _(mo, stage_2):
    award_table = mo.ui.table(
    stage_2,
    pagination=True,
    page_size=25,
    selection=None,
    show_column_summaries=False,
    show_data_types=True,
    show_download=True,
    show_search=True,
    max_columns=None,
    freeze_columns_left=["solicitationnumber", "title",],
    wrapped_columns=["title"], # , "attachment"],
    column_widths={
        "title": 200,
        "awarddescription": 460
    },
    label=f"Award notices",
    max_height=650,
    )
    mo.vstack([mo.md("## 2. Award notices"), award_table])
   
    return


@app.cell
def _(mo, stage_2):
    stage_2_agg = mo.sql(
        f"""
        SELECT 
        	noticetype as notice_type, 
        	COUNT(noticetype) as counter, 
        FROM stage_2 
        GROUP BY noticetype
        """
    )
    return


@app.cell
def _(mo, stage_2):
    stages = mo.sql(
        f"""
        SELECT
                        solicitationnumber,
            			title, 
                        COUNT(*) AS award_notice_count,
                        COUNT(DISTINCT contractnumber) AS contract_count,
                        MIN(contractawarddate) AS first_award_date,
                        MAX(contractawarddate) AS latest_award_date,
                        STRING_AGG(
                            DISTINCT supplierlegalname,
                            ', '
                        ) AS awarded_suppliers
                    FROM stage_2
                    WHERE solicitationnumber IS NOT NULL
                    GROUP BY solicitationnumber, title
        """
    )
    return


@app.cell
def _():
    return


@app.cell
def _(mo, rcmp_an):
    _df = mo.sql(
        f"""
        SELECT noticetype, COUNT(*) FROM rcmp_an GROUP BY noticetype 
        """
    )
    return


if __name__ == "__main__":
    app.run()
