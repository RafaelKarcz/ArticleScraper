===========================
Article Scraper Project
===========================

This project is a Python-based web scraping tool that retrieves articles from a specific webpage, filters them based on user-defined criteria, and saves them into organized directories. It utilizes `BeautifulSoup` for HTML parsing, `requests` for HTTP requests, and automates file handling to create a structured directory of the articles.

Environment Setup
-----------------

1. **Creating a New Conda Environment:**

   To create a new isolated environment for the project:

   .. code-block:: bash

      conda create --name articlescraper python=3.12

   This command creates a new environment named ``articlescraper`` with Python 3.12.

2. **Activating the Environment:**

   Activate the created environment with the following command:

   .. code-block:: bash

      conda activate articlescraper

   This ensures that any Python operations or package installations are confined to this environment.

3. **Installing Necessary Packages:**

   Install the required packages using the following command:

   .. code-block:: bash

      conda install beautifulsoup4 requests lxml

Project Overview
----------------

This project allows users to scrape and save articles from a webpage. The user inputs the number of pages to scrape and the desired article type. The scraper retrieves the articles, formats their titles as filenames, and saves the article text to `.txt` files in directories labeled by page number.

**Core Skills Demonstrated:**

- **Web Scraping**: Uses `BeautifulSoup` to parse the HTML content of webpages and locate specific elements like article titles and links.
- **HTTP Requests**: Utilizes the `requests` library to fetch webpage content.
- **File Management**: Automates the creation of directories and the saving of files, ensuring content is properly organized.
- **String Manipulation**: Cleans and formats article titles for use as filenames, ensuring they are valid and consistent.

Project Execution
-----------------

1. **Running the Article Scraper:**

   To run the project, navigate to the directory containing `article_scraper.py` and execute the script:

   .. code-block:: bash

      python article_scraper.py

2. **Functionality:**

   - **User Input**: Prompts the user to input the number of pages to scrape and the type of articles to save.
   - **Web Scraping**: Retrieves articles based on the input criteria, including filtering by article type.
   - **File Creation**: Automatically creates directories and saves the article text into `.txt` files named after the article titles.

Example Execution
-----------------

The program will prompt the user for the number of pages to scrape and the type of articles they want to save. Here's an example session:

.. code-block:: text

   Enter the number of pages to scrape: 2
   Enter the article type to filter (e.g., 'News'): Research Highlights
   Saved all articles.

Directory Structure:
--------------------

After running the script, your directory will be organized like this:

.. code-block:: text

   Project/
   ├── Page_1/
   │   ├── Article_1.txt
   │   ├── Article_2.txt
   ├── Page_2/
   │   ├── Article_1.txt
   │   └── Article_2.txt

Contributing
------------

Contributions to this project are welcome. Please ensure to maintain the environment specifications and follow the coding standards used in this project.

License
-------

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.

