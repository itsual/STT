import streamlit as st
import openai


# Define OpenAI API key
openai.api_key = "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"


def summarize(text):
    """Use OpenAI's GPT API to summarize the given text."""
    model_engine = "text-davinci-003"
    prompt = (f"Summarize the text below as a bullet point list of the most important points. Text: {text}\n Extract keywords from the below text. Keywords: Net sales, Operating income, Net income, revenue, operating expenses,  cash and cash equivalents,  investments, employed, people.\n\nSummary:")

    # Generate summary
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Return summary text
    summary = response.choices[0].text.strip()
    return summary


def extract_metrics(text):
    """Extract key financial metrics from the given text."""
    # TODO: Implement metric extraction

    # Example code to generate sample metrics
    metrics = [
        ("Revenue", 1000, 900),
        ("Net Profit", 100, 80),
        ("Earnings Per Share", 2.5, 2.0),
        ("Return on Equity", 0.15, 0.12),
        ("Debt-to-Equity Ratio", 1.5, 1.2),
        ("Dividend per Share", 1.0, 0.8),
        ("Operating Income", 150, 120),
        ("Region or Segment-wise Net Sales", 500, 400),
        ("Operating Expense", 80, 70),
    ]

    return metrics



def create_table(metrics):
    """Create a table of financial metrics."""
    headers = ["Metric", "Current Year", "Previous Year", "% Change"]
    rows = []

    for metric, current_year, previous_year in metrics:
        if current_year is None:
            current_year = "NA"
        if previous_year is None:
            previous_year = "NA"
        if current_year is None or previous_year is None:
            percent_change = "NA"
        else:
            percent_change = f"{(current_year - previous_year) / previous_year:.2%}"

        row = [metric, current_year, previous_year, percent_change]
        rows.append(row)

    st.table([headers] + rows)


def download_summary(summary, metrics):
    """Download summary and metrics as a CSV or PDF file."""
    # TODO: Implement file download
    pass


def main():
    # Set app title
    st.title("OpenAI ChatGPT Annual Report Summarizer")

    # Get URL input from user
    url = st.text_input("Enter the URL of the annual report document:")


    # Add button to summarize report
    if st.button("Summarize"):
        # TODO: Download PDF from URL
        # TODO: Extract text from PDF
        text = "Annual report text"

        # Summarize text
        summary = summarize(text)
        st.write("Summary:")
        summary_box = st.empty()
        with summary_box.container():
            st.write(summary)

        # Extract financial metrics
        metrics = extract_metrics(text)

        # Create table of financial metrics
        create_table(metrics)

        # Add button to download summary and metrics
        #file_format = st.selectbox("Choose file format:", ["CSV", "PDF"])
        #if st.button("Download"):
            #download_summary(summary, metrics, file_format)


if __name__ == "__main__":
    main()
