<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email
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
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/Chrono4/NovoLS">
    <img src="images/novols.jpg" alt="Logo" width="216" height="121">
  </a>

  <h3 align="center">NovoLS</h3>

  <p align="center">
    An unsupervised text simplification system.
    <br />
    <a href="https://github.com/Chrono4/NovoLS"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Chrono4/NovoLS">View Demo</a>
    ·
    <a href="https://github.com/Chrono4/NovoLS/issues">Report Bug</a>
    ·
    <a href="https://github.com/Chrono4/NovoLS/issues">Request Feature</a>
  </p>
</p>

<!-- ABOUT THE PROJECT -->
## About The Project

NovoLS is a lexical text simplification system which I constructed as part of my dissertation project. It is largely insipired by LightLS — an older lexcial text simplifier proposed by Prof. Dr. Goran Glavaš and Dr. Sanja Štajner in 2015. Both NovoLS and LightLS make use of GloVe word embeddings to find ‬simplification candidates for complex words, which are then ranked on a number of different features.

### Prerequisites

* [Gensim](https://radimrehurek.com/gensim/)
```sh
pip install gensim
```
* [NLTK](https://www.nltk.org/)
```sh
pip install nltk
```
* [Wordfreq](https://pypi.org/project/wordfreq/)
```sh
pip install wordfreq
```

### Installation

1. Clone the repo
```sh
git clone https://https://github.com/Chrono4/NovoLS.git
```

2. Install prerequisites

1. Run simplifier.py

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://https://github.com/Chrono4/NovoLS/issues) for a list of proposed features (and known issues).


<!-- CONTACT -->
## Contact

Your Name - [LinkedIn](https://www.linkedin.com/in/kane-miles-dev/)

Project Link: [https://https://github.com/Chrono4/NovoLS](https://https://github.com/Chrono4/NovoLS)

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

Shout out to Prof. Dr. Goran Glavaš for answering questions I had about the project. My dissertation would not have been what it was without his help. For those interested, a minimal version of Prof. Glavaš and Štajner's LightLS system can be found [here](https://github.com/codogogo/lightls)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo.svg?style=flat-square
[contributors-url]: https://https://github.com/Chrono4/NovoLS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo.svg?style=flat-square
[forks-url]: https://https://github.com/Chrono4/NovoLS/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo.svg?style=flat-square
[stars-url]: https://https://github.com/Chrono4/NovoLS/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo.svg?style=flat-square
[issues-url]: https://https://github.com/Chrono4/NovoLS/issues
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kane-miles-dev/
