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
    Report Generator for Binance Accounts!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
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
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

I made this project for myself to generate reports for my Binance account, then I decided to publish it as an opensource project for whom have the same needs.

<!-- GETTING STARTED -->

## Getting Started

Follow the following steps to install and run this project

### Prerequisites

- Requirements

  ```
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/EyasAnwar/safqti
   ```
2. Install Requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Copy .env.example to .env
4. Enter your API in `.env`
5. Run
   ```sh
   python main.py <options>
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

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

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
[product-screenshot]: images/screenshot.png
