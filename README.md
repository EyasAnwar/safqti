<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->

<a name="readme-top"></a>

<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Safqti</h3>

  <p align="center">
    Analyzing Binance Trades for Profitable Trading Insights.
    <br />
    <a href="https://github.com/EyasAnwar/safqti"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/EyasAnwar/safqti/issues">Report Bug</a>
    ·
    <a href="https://github.com/EyasAnwar/safqti/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributions">Contributions</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

Safqti is a Python project that leverages the Binance API to fetch and analyze account orders and transactions. It provides a convenient way to connect to the Binance cryptocurrency exchange, fetch historical account data, and store it in a PostgreSQL database. Furthermore, it performs comprehensive analysis on the inserted orders, generating a detailed report that includes crucial trade information such as buy price, sell price, profit, and duration of each trade.

### Features

- **Binance API Integration:** Safqti seamlessly connects to the Binance API, allowing users to access their account data securely and retrieve relevant information for analysis.

- **Order and Transaction Retrieval:** The project fetches all account orders and transactions from a specific date, ensuring comprehensive data coverage for analysis.

- **Database Integration:** Safqti employs a PostgreSQL database to store the fetched orders and transactions, providing a reliable and scalable solution for data storage.

- **Data Analysis and Reporting:** The project offers powerful analysis capabilities to interpret the inserted orders, enabling users to gain valuable insights into their trading activities. The generated report includes essential trade details such as buy price, sell price, profit, and trade duration, facilitating informed decision-making.

<!-- GETTING STARTED -->

## Getting Started

Follow the following steps to install and run this project

### Prerequisites

- Requirements

  ```
  pip install -r requirements.txt
  ```

### Installation

1. **Clone the repo**
   ```sh
   git clone https://github.com/EyasAnwar/safqti
   ```
2. **Installing Dependencies:** Safqti requires several Python dependencies. Install them by running the following command:
   ```sh
   pip install -r requirements.txt
   ```
3. **Setting Up Binance API:** To get started, obtain your Binance API credentials and ensure you have the necessary permissions to access account orders and transactions.
   - Copy .env.example to .env
   - Enter your API in `.env`
4. **Configuring the PostgreSQL Database:** Modify the project's configuration file to specify the PostgreSQL database connection details, such as host, port, username, password, and database name.
   - You can obtain the schema inside the `database.sql` file.
5. **Running the Project:** Execute the main script to start the Safqti application. It will connect to the Binance API, fetch orders and transactions, and insert them into the configured PostgreSQL database.
   ```sh
   python main.py --fetch_orders_history
   ```
6. **Generating the Trade Report:** After the data has been inserted into the database, run the analysis script to generate a comprehensive trade report. The report will provide valuable insights into each trade, including buy price, sell price, profit, and duration.

   ```sh
   python main.py --generate_trades_report
   ```

   <p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->

## Usage

```sh
usage: main.py [-h] [--fetch_orders_history] [--generate_trades_report]
               [--fetch_transactions_history]

Summarize your Binance account trades.

optional arguments:
  -h, --help            show this help message and exit
  --fetch_orders_history
                        Fetch Orders History
  --generate_trades_report
                        Generate Trades Report
  --fetch_transactions_history
                        Fetch Transactions History
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- Contributions -->

## Contributions

Contributions to Safqti are welcome! If you encounter any issues, have suggestions, or want to add new features, please submit an issue or a pull request. Together, we can enhance this project and make it even more useful for the trading community.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->

## License

Safqti is open source software released under the MIT License. Feel free to use, modify, and distribute the code according to the terms of this license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->

## Contact

Iyas Ashaikhkhalil - [Linkedin](https://www.linkedin.com/in/eyaskhalil/) - eyasanwar@gmail.com

Project Link: [https://github.com/EyasAnwar/safqti](https://github.com/EyasAnwar/safqti)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/EyasAnwar/safqti.svg?style=for-the-badge
[contributors-url]: https://github.com/EyasAnwar/safqti/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/EyasAnwar/safqti.svg?style=for-the-badge
[forks-url]: https://github.com/EyasAnwar/safqti/network/members
[stars-shield]: https://img.shields.io/github/stars/EyasAnwar/safqti.svg?style=for-the-badge
[stars-url]: https://github.com/EyasAnwar/safqti/stargazers
[issues-shield]: https://img.shields.io/github/issues/EyasAnwar/safqti.svg?style=for-the-badge
[issues-url]: https://github.com/EyasAnwar/safqti/issues
[license-shield]: https://img.shields.io/github/license/EyasAnwar/safqti.svg?style=for-the-badge
[license-url]: https://github.com/EyasAnwar/safqti/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/eyaskhalil
