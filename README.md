
<a name="readme-top"></a>

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

<h3 align="center">Python Low Pass</h3>

  <p align="center">
    A low pass first order filter in python with no libraries
    <br />
    <a href="https://github.com/Alexzander-Hurd/PythonLowPass"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Alexzander-Hurd/PythonLowPass/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Alexzander-Hurd/PythonLowPass/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
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
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

[![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these steps.

### Prerequisites

Python 3.8+ (You might already have python installed by default but if not follow these steps)
 * Debian/Ubuntu
  ```sh
  sudo apt-get update
  sudo apt-get install python3
  ```
 * Fedora/SUSE/RHEL
 ```sh
 sudo dnf install python3
 ```
 * Arch
 ```sh
 sudo pacman -Sy python-pip
 ```
 * Windows/Mac
 
 go to https://www.python.org/downloads/ then download and run the latest relevant installer (exe or pkg for win/mac respectively)
 

### Installation

* Clone the repo
   ```sh
   git clone https://github.com/Alexzander-Hurd/PythonLowPass.git
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

This tool is best used in the command line as it makes use of command line arguments


```sh
python filter.py < -i inputFile > < -o outputFile > < -a alphaValue > < -w windowSize >

python filter.py -i data.csv -o output.csv -a 0.5 -w 5
```
All the command line arguments are optional and will default the values in the example.

You can access this example by supplying `-h` or `--help` as the only argument


To customise these parameters using IDLE please see the IDLE documentation for customised run https://docs.python.org/3/library/idle.html#run-menu-editor-window-only

Using VS Code please see the following https://code.visualstudio.com/docs/python/debugging#_args

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

Your Name - ajghurd@gmail.com

Project Link: [https://github.com/Alexzander-Hurd/PythonLowPass](https://github.com/Alexzander-Hurd/PythonLowPass)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Alexzander-Hurd/PythonLowPass.svg?style=for-the-badge
[contributors-url]: https://github.com/Alexzander-Hurd/PythonLowPass/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Alexzander-Hurd/PythonLowPass.svg?style=for-the-badge
[forks-url]: https://github.com/Alexzander-Hurd/PythonLowPass/network/members
[stars-shield]: https://img.shields.io/github/stars/Alexzander-Hurd/PythonLowPass.svg?style=for-the-badge
[stars-url]: https://github.com/Alexzander-Hurd/PythonLowPass/stargazers
[issues-shield]: https://img.shields.io/github/issues/Alexzander-Hurd/PythonLowPass.svg?style=for-the-badge
[issues-url]: https://github.com/Alexzander-Hurd/PythonLowPass/issues
[license-shield]: https://img.shields.io/github/license/Alexzander-Hurd/PythonLowPass.svg?style=for-the-badge
[license-url]: https://github.com/Alexzander-Hurd/PythonLowPass/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/alexzanderhurd/
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
