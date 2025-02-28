# %%
import pandas as pd
from pathlib import Path
from pandas.api.types import CategoricalDtype

from utils import annotate_plot

# %%
response_file = Path("responses.csv")
data = pd.read_csv(
    response_file, skiprows=[0, 1], header=None, index_col=0, dtype=object
)

# These were test responses from Bryan and Kyle
drop_rows = [
    "3pcu3xeho94or13fmgo3pcu3vu7ufm3r",
    "gbeoi35j09sxzk2295regbeoi35w9xsn",
    "h3s656mrygc53ln0hik2h3s65acyqwhx",
]
data = data.drop(drop_rows)

# %%
operating_systems = [
    "macOS",
    "BSD",
    "Windows 7",
    "Windows 10",
    "Debian or its derivatives (Ubuntu, Mint, etc.)",
    "Red Hat or its derivatives (Fedora, CentOS, etc.)",
    "Other",
]
interfaces = ["Python", "MATLAB", "C++", "C", "Fortran"]
install_methods = [
    "I don't update",
    "Somebody else manages it for me",
    "Anaconda",
    "Build from source (via GitHub)",
    "Windows binaries (.msi file), downloaded from GitHub",
    "macOS installer (.pkg file), downloaded from GitHub",
    "Ubuntu Personal Package Archive (PPA)",
    "Other",
]
frequency = CategoricalDtype(["Often", "Sometimes", "Rarely", "Never"])

# %%
interface_data = data[range(8, 13)]
interface_data.columns = interfaces
n_responses = len(interface_data.index)
ax = (interface_data.count().sort_index() / n_responses).plot.barh()
annotate_plot(
    ax,
    f"Which interface(s) do you use to access Cantera? {n_responses} Responses",
    n_responses,
)

# %%
os_data = data[range(1, 8)]
os_data.columns = operating_systems
n_responses = len(os_data.index)
ax = (os_data.count().sort_index() / n_responses).plot.barh()
annotate_plot(
    ax, f"What operating system(s) do you use? {n_responses} Responses", n_responses
)

# %%
install_data = data[range(13, 21)]
install_data.columns = install_methods
n_responses = len(install_data.index)
ax = (install_data.count().sort_index() / n_responses).plot.barh()
annotate_plot(
    ax,
    "Do you use the following sources to install and/or upgrade Cantera?",
    n_responses,
)

# %%
ct_versions = CategoricalDtype(
    [
        "2.4 (released Aug. 2018)",
        "2.3 (released Jan. 2017)",
        "2.2 (released Jan. 2016)",
        "2.1 (released Apr. 2015)",
        "Older than 2.1",
        "Development version / master branch",
        "I’m not sure",
    ]
)
ct_version_data = data[21].dropna().astype(ct_versions)
n_responses = len(ct_version_data.index)
ax = (ct_version_data.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(ax, "What version of Cantera do you use most often?", n_responses)

# %%
python_freq_data = data[22].fillna("Never").astype(frequency)
n_responses = len(python_freq_data.index)
ax = (python_freq_data.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(ax, "How often do you use the Python interface?", n_responses)

# %%
python_versions = CategoricalDtype(["None"] + [f"3.{x}" for x in [5, 6, 7, 8]])
python_ver_data = data[23].fillna("None").astype(python_versions)
n_responses = len(python_ver_data.index)
ax = (python_ver_data.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(ax, "Which version of Python do you use the most?", n_responses)

# %%
matlab_freq_data = data[24].fillna("Never").astype(frequency)
n_responses = len(matlab_freq_data.index)
ax = (matlab_freq_data.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(ax, "How often do you use the MATLAB interface?", n_responses)

# %%
py_mat_freq_data = data[[22, 24]].fillna("Never").astype(frequency)
n_responses = len(py_mat_freq_data.index)
ax = (
    py_mat_freq_data.apply(pd.Series.value_counts).sort_index() / n_responses
).plot.barh()
ax.legend(["Python", "MATLAB"])
annotate_plot(
    ax, f"How often do you use the X interface? {n_responses} Responses", n_responses
)

# %%
continents = pd.CategoricalDtype(
    [
        "Africa",
        "Antarctica",
        "Asia",
        "Australia",
        "Europe",
        "North America",
        "South America",
    ]
)
location = data[105].astype(continents)
n_responses = len(location.index)
ax = (location.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(ax, f"Where do you live? {n_responses} Responses", n_responses)

# %%
support = data[98].astype("category")
n_responses = len(support.index)
ax = (support.value_counts().sort_index() / n_responses).plot.barh()
annotate_plot(
    ax,
    f"When you need help with Cantera, what is your_ first_ step to get support? {n_responses} Responses",
    n_responses,
)

# %%
donation = data[97].astype("category")
n_responses = len(donation.index)
ax = donation.value_counts(normalize=True).sort_index().plot.barh()
annotate_plot(
    ax,
    f"Have you ever made a tax-deductible donation to Cantera through NumFOCUS? {n_responses} Responses",
    n_responses,
)

# %%
