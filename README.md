# sec_gov_extract_info
# International Company Trading Data Extraction
## NEXT STEPS 
- [x] : [EXTRACT REPORTS](https://github.com/Nick2201/sec_gov_reports/issues/1)
- [x] : [EXTRACT DESCRIBE INFORMATION](https://github.com/Nick2201/extract_yf_api/issues/1)
- [ ] : [TRANSFORM AND ANALYSE]

![Python|100](http://ForTheBadge.com/images/badges/made-with-python.svg)
![Jupiter|100](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)

![Postgresql|100](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Linux|100](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

___
![License|100](https://img.shields.io/badge/License-MIT-green)
This Python project allows you to extract the current state of international companies trading on the USA stock market. It provides a set of tools to download and process the necessary data.

## Features

- Download and extract ZIP files containing trading data archives.
- Transform and load the extracted data into a database.
- Extract tickers for international companies.
- Load the extracted tickers into the database.

## Prerequisites

- Python 3.8 or higher

## Installation

1. Clone this repository to your local machine:

```bash
git clone git@github.com:Nick2201/sec_gov_extract_info.git
```

2. Navigate to the project directory:

```bash
cd sec_primary_info/sec_gov_extract_info
```

3. Install the dependencies using [Poetry](https://python-poetry.org/):

```bash
poetry install
poetry poetry shell
```

## Usage

The project provides the following command-line scripts:

- `archive_extract`: Downloads and extracts ZIP files containing trading data archives.
- `archive_load`: Transforms and loads the extracted data into a database.
- `tickers_extract`: Extracts tickers for international companies.
- `tickers_load`: Loads the extracted tickers into the database.

To use these scripts, run the following command:

```bash
poetry run <script-name>
```

Replace `<script-name>` with one of the script names mentioned above.

## Configuration

The project uses the [Poetry](https://python-poetry.org/) dependency manager and build tool. The project configuration can be found in the `pyproject.toml` file.

The tool scripts are configured in the `[tool.poetry.scripts]` section of the `pyproject.toml` file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or a pull request in the [repository](https://github.com/your-username/your-project).

## Acknowledgements

This project was inspired by the need to extract and analyze the current state of international companies trading on the USA stock market.

## Contact

For any questions or inquiries, please contact [nicklisits@gmail.com](mailto:your-email@example.com).
