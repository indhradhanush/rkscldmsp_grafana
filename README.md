<a name="readme-top"></a>
<!--
*** Thanks for checking out the Ruckus MSP Cloud monitoring with Grafana. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
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
  <a href="https://github.com/indhradhanush/rkscldmsp_grafana">
    <img src="docs/ruckusgrafanalogo.PNG" alt="Logo" width="388" height="327">
  </a>

  <h3 align="center">Ruckus MSP Cloud monitoring with Grafana</h3>

  <p align="center">
    This project is to pull data from Ruckus MSP Cloud API inventory and store in influxDB. Finally influxdb data is used as data source for Grafana. </BR> 
    <br />
    <a href="https://github.com/indhradhanush/rkscldmsp_grafana/docs"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#demo-pod">View Demo</a>
    ·
    <a href="https://github.com/indhradhanush/rkscldmsp_grafana/issues">Report Bug</a>
    ·
    <a href="https://github.com/indhradhanush/rkscldmsp_grafana/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#demo-pod">Demo</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://ruckus.cloud)

Ruckus MSP Cloud is a platform for managed service providers to manage and monitor their customers' Ruckus networks. It provides tools for remote network performance monitoring, account and billing management, and reporting.

Grafana is an open-source platform for data visualization and monitoring. It allows you to create, explore, and share dashboards and supports multiple backends for storing time series data. It is commonly used for DevOps, IoT, and real-time analytics.

 Grafana helps solving the MSP related problem where an MSP admin can do the following.</BR>
    1.	Single Dashboard to view all device status irrespective of tenant. </BR>
    2.	View limited monitoring information quickly about a tenant without must go to MSP inventory page.</BR>
    3.	Kiosk requirement – MSP admins often require Kiosk screen to show in a centralized NOC display, which allows quick glance of status of devices. Change settings token_rotation_interval_minutes and login_maximum_inactive_lifetime_days in Grafana.ini
    Grafana, an open-source tool is implemented as a separate system in a Linux machine. This is only a visualization tool, so it would need a time series database (TSDB) to visualize. In this guide dog we will use Influxdb as the TSDB.
To get the data from Ruckus MSP Cloud to Influxdb, Python program will be used. Python will retrieve data using Ruckus MSP API and moderate it before inserting into Influxdb.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Demo pod

Screenshots of the successful installation of Grafana, Python and Influx will result the following:

<a href="https://grafana.com/grafana/dashboards/17847">
    <img src="docs/Home.png" alt="Logo" >
</a>

* <a href="https://grafana.com/grafana/dashboards/17847">RUCKUS MSP Cloud Dashboard - Home : https://grafana.com/grafana/dashboards/17847</a>

<a href="https://grafana.com/grafana/dashboards/17852">
    <img src="docs/Tenant.png" alt="Logo" >
</a>

* <a href="https://grafana.com/grafana/dashboards/17852">RUCKUS MSP Cloud Dashboard - Tenant : https://grafana.com/grafana/dashboards/17852</a>

<a href="https://grafana.com/grafana/dashboards/17853">
    <img src="docs/Venue.png" alt="Logo" >
</a>

* <a href="https://grafana.com/grafana/dashboards/17853">RUCKUS MSP Cloud Dashboard - Venue : https://grafana.com/grafana/dashboards/17853</a>

<a href="https://grafana.com/grafana/dashboards/17854">
    <img src="docs/device.png" alt="Logo" >
</a>

* <a href="https://grafana.com/grafana/dashboards/17854">RUCKUS MSP Cloud Dashboard - Devices : https://grafana.com/grafana/dashboards/17854</a>


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* python3
  ```sh
  python3 app.py
  ```

### Installation

_Below is an example of how you can instruct your audience on installing and setting up your app. This template doesn't rely on any external dependencies or services._

1. Get a free API Key at [https://example.com](https://example.com)
2. Clone the repo
   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: docs/sysdes.PNG
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
