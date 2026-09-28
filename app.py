
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------------------------------
# LOGIN
# -------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

LOGIN_ID = "admin"
PASSWORD = "1234"

if not st.session_state.logged_in:

    st.markdown(
        "<h1 style='text-align:center;'>🩸 Blood Donor Connect</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='text-align:center;'>Welcome! Login to continue.</p>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        username = st.text_input("Login ID")
        password = st.text_input("Password", type="password")

        if st.button("Login", use_container_width=True):
            if username == LOGIN_ID and password == PASSWORD:
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Invalid Login ID or Password")

    st.stop()

# -------------------------------------------------
# CUSTOM DESIGN
# -------------------------------------------------

st.markdown("""
<style>
.stApp {
    background-color: #f7f9fc;
}

[data-testid="stSidebar"] {
    background-color: #ffffff;
}

.brand {
    font-size: 25px;
    font-weight: 800;
    color: #d92332;
    padding: 15px 0 25px 0;
}

.hero {
    background: linear-gradient(120deg, #fff1f2, #ffffff);
    border-radius: 24px;
    padding: 40px;
    border: 1px solid #f3d9dc;
    min-height: 280px;
}

.hero h1 {
    font-size: 42px;
    color: #182338;
}

.hero p {
    color: #667085;
    font-size: 18px;
}

.stat-card {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e8eaf0;
    margin-bottom: 15px;
}

.stat-title {
    color: #667085;
    font-size: 14px;
}

.stat-value {
    color: #182338;
    font-size: 30px;
    font-weight: 800;
}

.info-card {
    background: white;
    padding: 24px;
    border-radius: 16px;
    border: 1px solid #e8eaf0;
    min-height: 150px;
}

.info-card h3 {
    color: #182338;
}

.info-card p {
    color: #667085;
}

.footer {
    text-align: center;
    color: #98a2b3;
    padding: 30px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# SAMPLE DONOR DATA
# -------------------------------------------------

sample_data = [
    [1, "Arun Kumar", 21, "Male", "O+", "9876543210", "Chennai", "2024-02-14", "Available"],
    [2, "Priya Sharma", 19, "Female", "A+", "9123456780", "Coimbatore", "2024-03-10", "Available"],
    [3, "Karthik Raj", 24, "Male", "B+", "9988776655", "Madurai", "2024-01-20", "Unavailable"],
    [4, "Sneha R", 20, "Female", "O-", "9345678901", "Trichy", "2023-12-05", "Available"],
    [5, "Vignesh M", 23, "Male", "AB+", "9098765432", "Salem", "2024-04-18", "Available"],
    [6, "Divya S", 22, "Female", "B-", "9786123456", "Chennai", "2024-03-22", "Unavailable"],
    [7, "Rahul N", 25, "Male", "A-", "9887654321", "Erode", "2024-02-28", "Available"],
    [8, "Meena K", 18, "Female", "O+", "9123987654", "Coimbatore", "2024-01-15", "Available"],
    [9, "Suresh P", 27, "Male", "AB-", "9966778899", "Madurai", "2023-11-30", "Unavailable"],
    [10, "Anitha J", 21, "Female", "B+", "9345123789", "Trichy", "2024-04-05", "Available"],
    [11, "Mohan S", 26, "Male", "O+", "9876501234", "Salem", "2024-04-20", "Available"],
    [12, "Kavya R", 22, "Female", "A+", "9123405678", "Chennai", "2024-04-22", "Available"],
    [13, "Surya K", 23, "Male", "B+", "9988123456", "Erode", "2024-04-24", "Available"],
    [14, "Nithya P", 20, "Female", "O-", "9345012345", "Madurai", "2024-04-26", "Unavailable"],
    [15, "Ajay V", 25, "Male", "AB+", "9098123456", "Trichy", "2024-04-28", "Available"],
    [16, "Lakshmi S", 24, "Female", "B-", "9786012345", "Salem", "2024-05-01", "Available"],
    [17, "Dinesh R", 28, "Male", "A-", "9887012345", "Chennai", "2024-05-03", "Available"],
    [18, "Pooja M", 19, "Female", "O+", "9123012345", "Coimbatore", "2024-05-05", "Available"],
    [19, "Vijay K", 26, "Male", "AB-", "9966012345", "Madurai", "2024-05-07", "Unavailable"],
    [20, "Harini J", 21, "Female", "B+", "9345012345", "Trichy", "2024-05-09", "Available"],
    [21, "Sanjay Kumar", 22, "Male", "A+", "9876501111", "Chennai", "2024-05-10", "Available"],
    [22, "Deepa R", 20, "Female", "O+", "9876502222", "Salem", "2024-05-12", "Available"],
    [23, "Vimal S", 25, "Male", "B+", "9876503333", "Madurai", "2024-05-15", "Unavailable"],
    [24, "Keerthana P", 21, "Female", "AB+", "9876504444", "Coimbatore", "2024-05-18", "Available"],
    [25, "Ramesh K", 26, "Male", "O-", "9876505555", "Trichy", "2024-05-20", "Available"],
    [26, "Swetha M", 23, "Female", "A-", "9876506666", "Erode", "2024-05-22", "Available"],
    [27, "Aravind S", 24, "Male", "B-", "9876507777", "Chennai", "2024-05-25", "Available"],
    [28, "Pavithra J", 19, "Female", "AB-", "9876508888", "Salem", "2024-05-28", "Unavailable"],
    [29, "Manoj R", 27, "Male", "O+", "9876509999", "Madurai", "2024-05-30", "Available"],
    [30, "Aishwarya K", 22, "Female", "B+", "9876510000", "Coimbatore", "2024-06-02", "Available"],
    [31, "Gokul V", 25, "Male", "A+", "9876511111", "Trichy", "2024-06-05", "Available"],
    [32, "Ramya S", 20, "Female", "O-", "9876512222", "Erode", "2024-06-08", "Unavailable"],
    [33, "Hari K", 23, "Male", "AB+", "9876513333", "Chennai", "2024-06-10", "Available"],
    [34, "Nandhini P", 21, "Female", "B-", "9876514444", "Salem", "2024-06-12", "Available"],
    [35, "Kishore M", 28, "Male", "O+", "9876515555", "Madurai", "2024-06-15", "Available"],
    [36, "Anjali R", 22, "Female", "A-", "9876516666", "Coimbatore", "2024-06-18", "Available"],
    [37, "Prakash S", 26, "Male", "B+", "9876517777", "Trichy", "2024-06-20", "Unavailable"],
    [38, "Divya K", 19, "Female", "AB-", "9876518888", "Erode", "2024-06-22", "Available"],
    [39, "Sathish V", 24, "Male", "O-", "9876519999", "Chennai", "2024-06-25", "Available"],
    [40, "Monika J", 23, "Female", "A+", "9876520000", "Salem", "2024-06-28", "Available"],
    [41, "Karthik S", 25, "Male", "B-", "9876521111", "Madurai", "2024-07-01", "Available"],
    [42, "Megha R", 20, "Female", "O+", "9876522222", "Coimbatore", "2024-07-04", "Unavailable"],
    [43, "Suraj K", 27, "Male", "AB+", "9876523333", "Trichy", "2024-07-07", "Available"],
    [44, "Lavanya P", 22, "Female", "A-", "9876524444", "Erode", "2024-07-10", "Available"],
    [45, "Dinesh M", 26, "Male", "B+", "9876525555", "Chennai", "2024-07-12", "Available"],
    [46, "Shalini S", 21, "Female", "O-", "9876526666", "Salem", "2024-07-15", "Available"],
    [47, "Vasanth R", 24, "Male", "A+", "9876527777", "Madurai", "2024-07-18", "Unavailable"],
    [48, "Pooja K", 20, "Female", "AB-", "9876528888", "Coimbatore", "2024-07-20", "Available"],
    [49, "Naveen J", 28, "Male", "O+", "9876529999", "Trichy", "2024-07-22", "Available"],
    [50, "Harini V", 23, "Female", "B+", "9876530000", "Erode", "2024-07-25", "Available"],
]

columns = [
    "donor_id", "name", "age", "gender", "blood_group",
    "phone_number", "location", "donation_date", "status"
]

df = pd.DataFrame(sample_data, columns=columns)
df["donation_date"] = pd.to_datetime(df["donation_date"])

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.markdown(
    '<div class="brand">🩸 Blood Donor<br>Connect</div>',
    unsafe_allow_html=True
)

page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Dashboard",
        "Find Donors",
        "Donor Records",
        "Analytics",
        "About"
    ]
)

st.sidebar.divider()
st.sidebar.caption("Blood Donor Connect")
st.sidebar.caption("Simple • Clean • Modern")

if st.sidebar.button("Logout"):
    st.session_state.logged_in = False
    st.rerun()

# -------------------------------------------------
# HOME
# -------------------------------------------------

if page == "Home":

    st.markdown("""
    <div class="hero">
        <h1>A Single Donation<br>Can Save Lives</h1>
        <p>
        Every drop matters. Discover the importance of blood donation
        and explore donor information.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## 🩸 Give Blood. Give Hope.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>❤️ Save Lives</h3>
            <p>Your donation can help patients who need blood.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🤝 Build Community</h3>
            <p>Encourage a culture of helping others.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="info-card">
            <h3>📊 Explore Data</h3>
            <p>View donor information and useful statistics.</p>
        </div>
        """, unsafe_allow_html=True)

    st.info("Use the sidebar to explore the different pages.")

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

elif page == "Dashboard":

    st.title("📊 Dashboard")
    st.caption("Overview of blood donor information")

    total = len(df)
    available = len(df[df["status"] == "Available"])
    unavailable = total - available
    common_group = df["blood_group"].mode()[0]

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Total Donors</div>
            <div class="stat-value">{total}</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Available Donors</div>
            <div class="stat-value">{available}</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Unavailable</div>
            <div class="stat-value">{unavailable}</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-title">Common Blood Group</div>
            <div class="stat-value">{common_group}</div>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Donor Distribution")

    counts = df["blood_group"].value_counts().reset_index()
    counts.columns = ["Blood Group", "Donors"]

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            counts,
            x="Blood Group",
            y="Donors",
            title="Donor Count by Blood Group",
            color_discrete_sequence=["#e63946"]
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.pie(
            counts,
            names="Blood Group",
            values="Donors",
            title="Donor Percentage by Blood Group"
        )
        st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# FIND DONORS
# -------------------------------------------------

elif page == "Find Donors":

    st.title("🔍 Find Donors")
    st.caption("Search donors using the filters below.")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        blood = st.selectbox(
            "Blood Group",
            ["All"] + sorted(df["blood_group"].unique())
        )

    with col2:
        gender = st.selectbox(
            "Gender",
            ["All"] + sorted(df["gender"].unique())
        )

    with col3:
        location = st.selectbox(
            "Location",
            ["All"] + sorted(df["location"].unique())
        )

    with col4:
        status = st.selectbox(
            "Status",
            ["All"] + sorted(df["status"].unique())
        )

    filtered = df.copy()

    if blood != "All":
        filtered = filtered[filtered["blood_group"] == blood]

    if gender != "All":
        filtered = filtered[filtered["gender"] == gender]

    if location != "All":
        filtered = filtered[filtered["location"] == location]

    if status != "All":
        filtered = filtered[filtered["status"] == status]

    st.subheader(f"{len(filtered)} Donor(s) Found")

    st.dataframe(
        filtered,
        use_container_width=True,
        hide_index=True
    )

# -------------------------------------------------
# DONOR RECORDS
# -------------------------------------------------

elif page == "Donor Records":

    st.title("📋 Donor Records")
    st.caption("View and search donor information.")

    search = st.text_input("Search by name or location")

    records = df.copy()

    if search:
        records = records[
            records["name"].str.contains(search, case=False, na=False)
            | records["location"].str.contains(search, case=False, na=False)
        ]

    st.dataframe(
        records,
        use_container_width=True,
        hide_index=True
    )

    st.download_button(
        "⬇️ Download Donor Records",
        data=records.to_csv(index=False),
        file_name="donor_records.csv",
        mime="text/csv"
    )

# -------------------------------------------------
# ANALYTICS
# -------------------------------------------------

elif page == "Analytics":

    st.title("📈 Analytics")
    st.caption("Visual insights from donor data.")

    col1, col2 = st.columns(2)

    with col1:
        gender_counts = df["gender"].value_counts().reset_index()
        gender_counts.columns = ["Gender", "Donors"]

        fig = px.pie(
            gender_counts,
            names="Gender",
            values="Donors",
            title="Donor Distribution by Gender",
            hole=0.4
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        location_counts = df["location"].value_counts().reset_index()
        location_counts.columns = ["Location", "Donors"]

        fig = px.bar(
            location_counts,
            x="Location",
            y="Donors",
            title="Donors by Location",
            color_discrete_sequence=["#e63946"]
        )
        st.plotly_chart(fig, use_container_width=True)

    trend = (
        df.groupby("donation_date")
        .size()
        .reset_index(name="Donations")
        .sort_values("donation_date")
    )

    fig = px.line(
        trend,
        x="donation_date",
        y="Donations",
        markers=True,
        title="Donations Over Time",
        color_discrete_sequence=["#e63946"]
    )

    st.plotly_chart(fig, use_container_width=True)

# -------------------------------------------------
# ABOUT
# -------------------------------------------------

elif page == "About":

    st.title("🩸 About Blood Donation")

    st.write("""
    Blood donation is a voluntary act of giving blood to help people
    who need transfusions during medical treatment, emergencies,
    surgeries, and other situations.

    Blood contains red blood cells, plasma, and platelets.
    Each component plays an important role in supporting patients.
    """)

    st.subheader("Why Is Blood Donation Important?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-card">
            <h3>❤️ Helps Patients</h3>
            <p>
            Donated blood supports hospitals in treating patients
            who require blood transfusions.
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-card">
            <h3>🤝 Supports Communities</h3>
            <p>
            Voluntary blood donation helps maintain blood supplies
            for people in need.
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("Who Can Donate?")

    st.write("""
    Eligibility depends on age, health, medical history, and local
    blood-donation guidelines. A qualified healthcare professional
    or blood bank can confirm whether someone is eligible to donate.
    """)

    st.warning(
        "Always follow the advice of qualified healthcare professionals "
        "and your local blood bank before donating."
    )

    st.success("Donate blood when eligible. Help make a difference.")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("""
<div class="footer">
    Blood Donor Connect | Donate Blood, Give Hope ❤️
</div>
""", unsafe_allow_html=True)