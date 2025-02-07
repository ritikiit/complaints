{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "from streamlit.components.v1 import html\n",
    "\n",
    "# Set up the page\n",
    "st.set_page_config(\n",
    "    page_title=\"Bangalore Real Estate Insights\",\n",
    "    page_icon=\"🏙️\",\n",
    "    layout=\"wide\"\n",
    ")\n",
    "\n",
    "# Add a title and description\n",
    "st.title(\"Bangalore Real Estate Hotspots\")\n",
    "st.markdown(\"\"\"\n",
    "**Visualize complaint data** to identify high-potential areas for real estate development.\n",
    "- Use the map to analyze infrastructure issues\n",
    "- Identify areas with high complaint density\n",
    "- Generate targeted leads for marketing\n",
    "\"\"\")\n",
    "\n",
    "# Load and display the HTML map\n",
    "def load_map():\n",
    "    with open(\"bangalore_complaints_map.html\", \"r\", encoding=\"utf-8\") as f:\n",
    "        return f.read()\n",
    "\n",
    "# Display the map\n",
    "html(load_map(), height=700)\n",
    "\n",
    "# Add a sidebar for filters (optional)\n",
    "with st.sidebar:\n",
    "    st.header(\"Filters\")\n",
    "    st.markdown(\"Customize your analysis:\")\n",
    "    selected_area = st.selectbox(\"Select Area\", [\"All\", \"Central\", \"East\", \"North\"])\n",
    "    st.checkbox(\"Show Heatmap\", True)\n",
    "    st.checkbox(\"Show Property Prices\", False)"
   ]
  }
 ],
 "metadata": {
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
