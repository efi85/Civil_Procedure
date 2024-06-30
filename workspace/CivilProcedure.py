import streamlit as st

def litigation_flow():
    st.title("Litigation Flow Chart")

    st.header("1. Summons")
    st.header("2. Appearance/Notice of Intention to Defend")
    appearance = st.radio("Did the defendant appear or file a notice of intention to defend?", ('Yes', 'No'))

    if appearance == 'No':
        st.header("3. Request for Default Judgment")
        default_judgment = st.radio("Was a request for default judgment made?", ('Yes', 'No'))
        if default_judgment == 'Yes':
            st.header("Judgment")
            st.stop()

    st.header("4. Plea")
    plea = st.radio("Was a plea filed?", ('Yes', 'No'))

    if plea == 'No':
        st.header("Notice of Bar / Notice to Plead")
        notice_to_plead = st.radio("Was a notice of bar or notice to plead filed?", ('Yes', 'No'))
        if notice_to_plead == 'Yes':
            plea_after_notice = st.radio("Was a plea filed after notice?", ('Yes', 'No'))
            if plea_after_notice == 'No':
                st.header("Judgment")
                st.stop()

    st.header("5. Summary Judgment")
    summary_judgment = st.radio("Was a summary judgment requested?", ('Yes', 'No'))
    if summary_judgment == 'Yes':
        st.header("Judgment")
        st.stop()

    st.header("6. Counterclaim")
    counterclaim = st.radio("Was a counterclaim filed?", ('Yes', 'No'))

    if counterclaim == 'Yes':
        st.header("7. Plea to Counterclaim")
        plea_to_counterclaim = st.radio("Was a plea to counterclaim filed?", ('Yes', 'No'))
        if plea_to_counterclaim == 'No':
            st.header("Notice of Bar / Notice to Plead")
            notice_to_plead_counter = st.radio("Was a notice of bar or notice to plead filed?", ('Yes', 'No'))
            if notice_to_plead_counter == 'Yes':
                plea_to_counterclaim_after_notice = st.radio("Was a plea to counterclaim filed after notice?", ('Yes', 'No'))
                if plea_to_counterclaim_after_notice == 'No':
                    st.header("Judgment on Counterclaim")
                    st.stop()

    st.header("8. Close of Pleadings")
    st.header("9. Discovery Notices")
    st.header("10. Request for Further Particulars for the Purposes of Trial")
    st.header("11. Rule 24 Notices / Rule 36 Notices")
    st.header("12. Notice of Set Down")
    st.header("13. Subpoenas")
    st.header("14. Discovery Affidavit")
    st.header("15. Expert Notices")
    st.header("16. Pre-trial conference/Directions Hearing")
    st.header("17. Pre-trial Consultations")
    st.header("18. Trial Bundles")
    st.header("19. Replication/Reply")
    st.header("20. Trial")
    st.header("21. Judgment")
    st.header("22. Judgment on Counterclaim (if applicable)")

if __name__ == "__main__":
    litigation_flow()
