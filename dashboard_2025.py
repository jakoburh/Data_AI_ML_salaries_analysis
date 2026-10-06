
import pandas as pd
import streamlit as st
import altair as alt
#pip install openpyxl #inštalira openpyxl ki omogoča branje excela 
#streamlit run "C:\Users\Jakob Urh\Desktop\Statistics\salaries\dashboard.py"  #zažene to kodo v streamlitu
@st.cache_data # tole pove, da si streamlit zapomne naslednjo funkcijo in je ne poganja ob vsakem zagonu, razen če pride do spremembe funkcije/excela
def load_data():
    df = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx", sheet_name="podatki")
    return df
#funkcija load_data poišče excel datoteko in jo naloži
df = load_data() #prebere excel
st.title("AI, ML and DATA salaries analysis (2020–2025)") #naslov
st.write("This dashboard provides an interactive exploration of salaries in data-related professions between 2020 and 2025. It allows users to filter, compare, and visualize salary data by various factors. ")

st.write("It is intended as an exploratory tool for recruiters, job seekers, and anyone interested in salary patterns in the data industry.The dataset is sourced from kaggle, cleaned and processed to highlight trends, distributions, and differences across professions, regions, and work arrangements.")

#IZBIRANJE PARAMETROV
experience_options = ["Junior", "Intermediate", "Senior", "Executive", "All"] #množica unikatnih vseh nivo izkušenj, pretvorba v seznam
group_title_options =  df["Grouped_title"].unique().tolist()
title_options=df["job_title"].unique().tolist()
group_title_options.insert(0, "None") #velja le za sezname #.insert (mesto_vstavitve, kaj_vstavimo)
title_options.insert(0, "None")


experience = st.selectbox("Pick experience level:", experience_options) #izbereš nivo, ki te zanima
group_title = st.selectbox("Pick group title:", group_title_options) #izbereš groupiran poklic
title=st.selectbox("Pick specific title:", title_options) #izbereš poklic

#preglednica_podatkov=pd.read_excel("salaries_analysis.xlsx",sheet_name="podatki",usecols="A:M",skiprows=1,nrows=136758,header=None)
#preglednica_podatkov.columns = ["work_year", "experience_level", "employment_type", "job_title", "salary", "salary_currency", "salary_in_usd",
#                               "employee_residence", "remote_ratio", "company_locatio", "company_size", "salary(EUR)", 
#                               "grouped_title"]
#preglednica_podatkov = preglednica_podatkov.dropna(subset=["job_title"])
#if title in preglednica_podatkov["job_title"].values:
#    grouped = preglednica_podatkov.loc[preglednica_podatkov["job_title"] == title, "grouped_title"].values[0]
#    st.write(f"{title} was grouped under **{grouped}**")
#else:
#    st.warning("Izbrani poklic ni bil najden v podatkih.")

#IZPIS POVPREČJA, MEDIANE, DELA OD DOMA
if group_title!="None" and title!="None":
    st.warning("Pick either job title or grouped title")
    st.stop()
if group_title=="None" and title=="None":
    st.stop()

#IZPIS POVPREČNE PLAČE
#ZA GROUPIRANE POKLICE

preglednica_pp = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx", sheet_name="analiza2", usecols="H:R", skiprows=83, nrows=20)
preglednica_pp.columns = ["grouped_title", "junior_salary", "junior_count","intermediate_salary", "intermediate_count","senior_salary", "senior_count","executive_salary", "executive_count","total_avg_salary", "total_count"]
preglednica_pp = preglednica_pp.dropna(subset=["grouped_title"])
vrstica = preglednica_pp[preglednica_pp["grouped_title"] == group_title]

preglednica_mediana = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx",sheet_name="analiza3",usecols="M:R",skiprows=15,nrows=20,header=None)
preglednica_mediana.columns = ["grouped_title", "junior_mediana", "intermediate_mediana","senior_mediana", "executive_mediana", "all_mediana"]
vrstica2 = preglednica_mediana[preglednica_mediana["grouped_title"] == group_title]
preglednica_mediana = preglednica_mediana.dropna(subset=["grouped_title"])

preglednica_remote = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx",sheet_name="analiza4",usecols="G:AP",skiprows=6,nrows=20,header=None) #35 stolpcev
preglednica_remote.columns = ["grouped_title", "junior_office","junior_office_count", "junior_hybrid","junior_hybrid_count", "junior_remote", "junior_remote_count", "junior_salary", "junior_count",
                                "intermediat_office","intermediat_office_count", "intermediat_hybrid","intermediat_hybrid_count", "intermediat_remote", "intermediat_remote_count", "intermediat_salary", "intermediat_count",
                                "senior_office","senior_office_count", "senior_hybrid","senior_hybrid_count", "senior_remote", "senior_remote_count", "senior_salary", "senior_count",
                                "executive_office","executive_office_count", "executive_hybrid","executive_hybrid_count", "executive_remote", "executive_remote_count", "executive_salary", "executive_count",
                                "all_salary", "all_count","percentage"]
vrstica3= preglednica_remote[preglednica_remote["grouped_title"] == group_title]
preglednica_remote= preglednica_remote.dropna(subset=["grouped_title"])


if title=="None":     
    if experience == "Junior":
        stevec=vrstica.iloc[0]["junior_count"]
        izbrana_placa = vrstica.iloc[0]["junior_salary"] #iloc = index location, izberi prvo vrstico po indeksu
        izbrana_mediana = vrstica2.iloc[0]["junior_mediana"]
        izbrana_remote_placa = vrstica3.iloc[0]["junior_remote"]
        izbrana_remote_delez = round(((vrstica3.iloc[0]["junior_remote_count"])/(vrstica3.iloc[0]["all_count"]))*100,2)
    elif experience == "Intermediate":
        stevec=vrstica.iloc[0]["intermediate_count"]
        izbrana_placa = vrstica.iloc[0]["intermediate_salary"]
        izbrana_mediana = vrstica2.iloc[0]["intermediate_mediana"]
        izbrana_remote_placa = vrstica3.iloc[0]["intermediat_remote"]
        izbrana_remote_delez = round(((vrstica3.iloc[0]["intermediat_remote_count"])/(vrstica3.iloc[0]["all_count"]))*100,2)
    elif experience == "Senior":
        stevec=vrstica.iloc[0]["senior_count"]
        izbrana_placa = vrstica.iloc[0]["senior_salary"]
        izbrana_mediana = vrstica2.iloc[0]["senior_mediana"]
        izbrana_remote_placa = vrstica3.iloc[0]["senior_remote"]
        izbrana_remote_delez = round(((vrstica3.iloc[0]["senior_remote_count"])/(vrstica3.iloc[0]["all_count"]))*100,2)
    elif experience == "Executive":
        stevec=vrstica.iloc[0]["executive_count"]
        izbrana_placa = vrstica.iloc[0]["executive_salary"]
        izbrana_mediana = vrstica2.iloc[0]["executive_mediana"]
        izbrana_remote_placa = vrstica3.iloc[0]["executive_remote"]
        izbrana_remote_delez = round(((vrstica3.iloc[0]["executive_remote_count"])/(vrstica3.iloc[0]["all_count"]))*100,2)
    elif experience == "All":
        stevec=vrstica.iloc[0]["total_count"]
        izbrana_placa = vrstica.iloc[0]["total_avg_salary"]
        izbrana_mediana = vrstica2.iloc[0]["all_mediana"]
        izbrana_remote_placa = (vrstica3.iloc[0]["junior_remote"]+vrstica3.iloc[0]["intermediat_remote"]+vrstica3.iloc[0]["senior_remote"]+vrstica3.iloc[0]["executive_remote"])/4
        izbrana_remote_delez = round(((vrstica3.iloc[0]["junior_remote_count"]+vrstica3.iloc[0]["intermediat_remote_count"]+vrstica3.iloc[0]["senior_remote_count"]+vrstica3.iloc[0]["executive_remote_count"])/(vrstica3.iloc[0]["all_count"]))*100,2)

    if pd.isna(izbrana_mediana):  # ✅ POPRAVEK 5
        st.warning("Data for calculating median value for salary is incomplete. Please pick another search parameters.")
    else:
        formatted = f"{izbrana_mediana:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        st.write(f"📌 Median value for ({group_title}) ({experience}): {formatted}€")

    if izbrana_mediana=="#DIV/0!":
        st.write("Data for calculating median value for salary is incomplete. Please change the search parameters.")
        
    if pd.isna(izbrana_placa):
        st.warning("Data for calculating average salary is incomplete. Please change the search parameters.")
    else:
        formatted = f"{izbrana_placa:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        st.write(f"📌 Average salary for {group_title} ({experience}): {formatted}€")

    if pd.isna(izbrana_remote_placa) or pd.isna(izbrana_remote_delez):
        st.warning("Data for calculating average remote salary and ratio is incomplete. Please change the search parameters.")
    else:
        formatted = f"{izbrana_remote_placa:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
        st.write(f"📌 {izbrana_remote_delez}% of all {group_title} ({experience}) have a remote job with their average salary: {formatted}€")
 
#ZA POSAMEZNE POKLICE           
if title!="None":
    preglednica_po2 = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx", sheet_name="analiza20", usecols="A:K",skiprows=3, nrows=398, header=None)
    preglednica_po2.columns = ["job_title", "junior_salary", "junior_count","intermediate_salary", "intermediate_count","senior_salary", "senior_count","executive_salary", "executive_count","total_avg_salary", "total_count"]
    preglednica_po2 = preglednica_po2.dropna(subset=["job_title"])
    vrstica2 = preglednica_po2[preglednica_po2["job_title"] == title]


    preglednica_mediana2 = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx",sheet_name="analiza3",usecols="F:K",skiprows=4,nrows=398,header=None)
    preglednica_mediana2.columns = ["job_title", "junior_mediana", "intermediate_mediana","senior_mediana", "executive_mediana", "all_mediana"]
    vrstica22 = preglednica_mediana2[preglednica_mediana2["job_title"] == title]
    preglednica_mediana2 = preglednica_mediana2.dropna(subset=["job_title"])

    preglednica_remote2 = pd.read_excel(r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx",sheet_name="analiza4",usecols="G:AO",skiprows=30,nrows=398,header=None) #35 stolpcev
    preglednica_remote2.columns = ["job_title", "junior_office","junior_office_count", "junior_hybrid","junior_hybrid_count", "junior_remote", "junior_remote_count", "junior_salary", "junior_count",
                                "intermediat_office","intermediat_office_count", "intermediate_hybrid","intermediate_hybrid_count", "intermediate_remote", "intermediat_remote_count", "intermediat_salary", "intermediat_count",
                                "senior_office","senior_office_count", "senior_hybrid","senior_hybrid_count", "senior_remote", "senior_remote_count", "senior_salary", "senior_count",
                                "executive_office","executive_office_count", "executive_hybrid","executive_hybrid_count", "executive_remote", "executive_remote_count", "executive_salary", "executive_count",
                                "all_salary", "all_count"]
    vrstica32= preglednica_remote2[preglednica_remote2["job_title"] == title]
    preglednica_remote2= preglednica_remote2.dropna(subset=["job_title"])

 
    if group_title=="None": #preveri če tabela ni prazna
        if experience == "Junior":
            stevec2=vrstica2.iloc[0]["junior_count"]
            izbrana_placa2 = vrstica2.iloc[0]["junior_salary"] #iloc = index location, izberi prvo vrstico po indeksu
            izbrana_mediana2 = vrstica22.iloc[0]["junior_mediana"]
            izbrana_remote_placa2 = vrstica32.iloc[0]["junior_remote"]
            izbrana_remote_delez2 = round(((vrstica32.iloc[0]["junior_remote_count"])/(vrstica32.iloc[0]["all_count"]))*100,2)
        elif experience == "Intermediate":
            stevec2=vrstica2.iloc[0]["intermediate_count"]
            izbrana_placa2 = vrstica2.iloc[0]["intermediate_salary"]
            izbrana_mediana2 = vrstica22.iloc[0]["intermediate_mediana"]
            izbrana_remote_placa2 = vrstica32.iloc[0]["intermediate_remote"]
            izbrana_remote_delez2 = round(((vrstica32.iloc[0]["intermediat_remote_count"])/(vrstica32.iloc[0]["all_count"]))*100,2)
        elif experience == "Senior":
            stevec2=vrstica2.iloc[0]["senior_count"]
            izbrana_placa2 = vrstica2.iloc[0]["senior_salary"]
            izbrana_mediana2 = vrstica22.iloc[0]["senior_mediana"]
            izbrana_remote_placa2 = vrstica32.iloc[0]["senior_remote"]
            izbrana_remote_delez2 = round(((vrstica32.iloc[0]["senior_remote_count"])/(vrstica32.iloc[0]["all_count"]))*100,2)
        elif experience == "Executive":
            stevec2=vrstica2.iloc[0]["executive_count"]
            izbrana_placa2 = vrstica2.iloc[0]["executive_salary"]
            izbrana_mediana2 = vrstica22.iloc[0]["executive_mediana"]
            izbrana_remote_placa2 = vrstica32.iloc[0]["executive_remote"]
            izbrana_remote_delez2 = round(((vrstica32.iloc[0]["executive_remote_count"])/(vrstica32.iloc[0]["all_count"]))*100,2)
        elif experience == "All":
            stevec2=vrstica2.iloc[0]["total_count"]
            izbrana_placa2 = vrstica2.iloc[0]["total_avg_salary"]
            izbrana_mediana2 = vrstica22.iloc[0]["all_mediana"]
            izbrana_remote_placa2 = (vrstica32.iloc[0]["junior_remote"]+vrstica32.iloc[0]["intermediat_remote"]+vrstica32.iloc[0]["senior_remote"]+vrstica32.iloc[0]["executive_remote"])/4
            izbrana_remote_delez2 = round(((vrstica32.iloc[0]["junior_remote_count"]+vrstica32.iloc[0]["intermediat_remote_count"]+vrstica32.iloc[0]["senior_remote_count"]+vrstica32.iloc[0]["executive_remote_count"])/(vrstica32.iloc[0]["all_count"]))*100,2)
        
        if pd.isna(izbrana_mediana2): 
             st.warning("Data for calculating median value for salary is incomplete. Please change the search parameters.")
        else:
            formatted = f"{izbrana_mediana2:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
            st.write(f"📌 Median value for ({title}) ({experience}): {formatted}€")

        if pd.isna(izbrana_remote_placa2) or pd.isna(izbrana_remote_delez2):
            st.warning("Data for calculating average remote salary and ratio is incomplete. Please change the search parameters.")
        else:
            formatted = f"{izbrana_remote_placa2:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
            st.write(f"📌 {izbrana_remote_delez2}% of all {title} ({experience}) have a remote job with their average salary: {formatted}€")
        if pd.isna(izbrana_placa2):
            st.warning("Data for calculating average salary is incomplete. Please change the search parameters.")
        else:
            formatted = f"{izbrana_placa2:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")
            st.write(f"📌 Average salary for {title} ({experience}): {formatted}€")
    if stevec2 < 5:
        st.error(f"Dataset contains {stevec2} job titles. 🚨 Calculations are very unreliable.")
    elif stevec2 < 10:
        st.warning(f"Dataset contains {stevec2} job titles. ⚠️ Calculations are not very reliable.")
    elif stevec2 < 30:
        st.info(f"Dataset contains {stevec2} job titles. ✅ Calculations are moderately reliable.")
    else:
        st.success(f"Dataset contains {stevec2} job titles. ✅✅ Calculations are very reliable.")
if title=="None":
    if stevec < 5:
        st.error(f"Dataset contains {stevec} job titles. 🚨 Calculations are very unreliable.")
    elif stevec < 10:
        st.warning(f"Dataset contains {stevec} job titles. ⚠️ Calculations are not very reliable.")
    elif stevec < 30:
        st.info(f"Dataset contains {stevec} job titles. ✅ Calculations are moderately reliable.")
    else:
        st.success(f"Dataset contains {stevec} job titles. ✅✅ Calculations are very reliable.")


st.subheader("Average salaries per grouped titles")
chart_data = preglednica_pp[["grouped_title", "total_avg_salary"]]#.dropna()

chart = (alt.Chart(chart_data).mark_bar().encode(
            x=alt.X("total_avg_salary:Q", title="Average salary (€)"), # nanaša na oznako v dataframeu in tip podatka; q=quantitative/številke
            y=alt.Y("grouped_title:N", sort="-x", title="Grouped title"), #n=nominal/besede, o=ordinal/urejene kategorije, t=temporal/datumi
            tooltip=[alt.Tooltip("grouped_title", title="Grouped title"),alt.Tooltip("total_avg_salary", title="Average salary (€)", format=",.0f")]
        )
        .properties(height=700)
    )

st.altair_chart(chart, use_container_width=True)


st.subheader("Median values per grouped titles")
chart_data = preglednica_mediana[["grouped_title","all_mediana"]].dropna(subset=["all_mediana"])

chart2 = (alt.Chart(chart_data).mark_bar().encode(
            x=alt.X("all_mediana:Q", title="Median salary (€)"), # nanaša na oznako v dataframeu in tip podatka; q=quantitative/številke
            y=alt.Y("grouped_title:N", sort="-x", title="Grouped title"), #n=nominal/besede, o=ordinal/urejene kategorije, t=temporal/datumi
            tooltip=[alt.Tooltip("grouped_title", title="Grouped title"),alt.Tooltip("all_mediana", title="Median (€)", format=",.0f")]
        )
        .properties(height=400)
    )

st.altair_chart(chart2, use_container_width=True)


st.subheader("Remote work percentage within grouped title")
chart_data = preglednica_remote[["grouped_title","percentage"]].dropna(subset=["percentage"])

chart3 = (alt.Chart(chart_data).mark_bar().encode(
            x=alt.X("percentage:Q", title="Percentage of remote work (%)"), 
            y=alt.Y("grouped_title:N", sort="-x", title="Grouped title"), 
            tooltip=[alt.Tooltip("grouped_title", title="Grouped title"),alt.Tooltip("percentage", title="Percentage (%)", format=",.0f")]
        )
        .properties(height=600)
    )

st.altair_chart(chart3, use_container_width=True)


st.header("🛠️ Custom Graph")

@st.cache_data
def load_podatki(path=r"C:\Users\Jakob Urh\Desktop\Statistics\salaries\salaries_analysis.xlsx"):
    df = pd.read_excel(path, sheet_name="podatki")
    # standardiziraj tipe
    if "Salary (EUR)" in df.columns:
        df["Salary (EUR)"] = pd.to_numeric(df["Salary (EUR)"], errors="coerce")
    # remote_ratio zna biti string z vejico/piko ali "-", pretvori v število
    df["remote_ratio_num"] = pd.to_numeric(df.get("remote_ratio"), errors="coerce")
    return df

pdf = load_podatki()

# --- 1) Izbira scope + takoj izbor All ali Specific ---
scope = st.radio("What are you looking for?", ["Grouped titles", "Job titles", "None"], horizontal=True)

scope_col, scope_val = None, None
if scope == "Grouped titles":
    if "Grouped_title" not in pdf.columns:
        st.error("V listu 'podatki' manjka stolpec 'Grouped_title'.")
        st.stop()
    opts = ["All"] + sorted([v for v in pdf["Grouped_title"].dropna().unique()])
    chosen = st.selectbox("Pick a grouped title:", opts)
    scope_col = "Grouped_title"
    scope_val = None if chosen == "All" else chosen

elif scope == "Job titles":
    if "job_title" not in pdf.columns:
        st.error("V listu 'podatki' manjka stolpec 'job_title'.")
        st.stop()
    opts = ["All"] + sorted([v for v in pdf["job_title"].dropna().unique()])
    chosen = st.selectbox("Pick a job title:", opts)
    scope_col = "job_title"
    scope_val = None if chosen == "All" else chosen
else:
    st.info("If you choose None, the graph will not be created.")

# --- 2) X in Y osi ---
# X: leto, lokacija, employment type
x_map = {
    "Year": "work_year",
    "Location (company)": "company_location",
    "Employment type": "employment_type",
}
# pokaži samo tiste, ki res obstajajo
x_candidates = [label for label, col in x_map.items() if col in pdf.columns]
x_label = st.selectbox("X-axis", x_candidates)
x_col = x_map[x_label]

# Y: povprečna plača, mediana, remote %
y_map = {
    "Average salary (€)": "avg_salary",
    "Median salary (€)": "median_salary",
    "Remote percentage (%)": "remote_pct",
}
y_label = st.selectbox("Y-axis", list(y_map.keys()))
y_metric = y_map[y_label]

# --- 3) Filtriranje glede na scope ---
df = pdf.copy()
if scope_col:
    if scope_val is not None:  # Specific
        df = df[df[scope_col] == scope_val]
    # All = brez dodatnega filtra

# --- 4) Agregacija po X za izbrano Y metriko ---
if scope == "None":
    st.stop()

if df.empty:
    st.warning("No data for the chosen parameters.")
    st.stop()

if "Salary (EUR)" not in df.columns:
    st.error("V 'podatki' manjka stolpec 'Salary (EUR)'.")
    st.stop()

g = df.groupby(x_col, dropna=False)

if y_metric == "avg_salary":
    out = g["Salary (EUR)"].mean(numeric_only=True).reset_index(name="value")
elif y_metric == "median_salary":
    out = g["Salary (EUR)"].median(numeric_only=True).reset_index(name="value")
else:  # remote_pct
    if "remote_ratio_num" not in df.columns:
        st.error("V 'podatki' manjka 'remote_ratio' za izračun % remote.")
        st.stop()
    out = g.apply(lambda s: (s["remote_ratio_num"] == 100).mean() * 100).reset_index(name="value")

# očisti in nariši
out = out.dropna(subset=["value"])
# pretvori X v niz (boljši prikaz kategorij); leto lahko ostane int, ni kritično
if out[x_col].dtype == "object":
    out[x_col] = out[x_col].astype(str)

if out.empty:
    st.warning("Po agregaciji ni podatkov (same manjkajoče vrednosti).")
else:
    height = max(300, len(out) * 26)
    chart = (
        alt.Chart(out)
        .mark_bar()
        .encode(
            x=alt.X("value:Q", title=y_label),
            y=alt.Y(f"{x_col}:N", sort="-x", title=x_label),
            tooltip=[alt.Tooltip(f"{x_col}:N", title=x_label),
                     alt.Tooltip("value:Q", title=y_label, format=",.1f")]
        )
        .properties(height=height)
    )
    st.altair_chart(chart, use_container_width=True)

    st.caption(
        f"Number of elements on X-axis: {len(out)} • "
        f"Minimal value: {out['value'].min():,.1f} • "
        f"Median value: {out['value'].median():,.1f} • "
        f"Maximum value: {out['value'].max():,.1f}"
    )
if x_label=="Employment type":
    st.write ("FT: Full-time")
    st.write("PT: Part-time")
    st.write("CT: Contract")
    st.write("FL: Freelance")
if x_label=="Location (company)":
    st.markdown('<a href="https://www.iban.com/country-codes" target="_blank">List for two letter country abbreviation</a>',unsafe_allow_html=True)
