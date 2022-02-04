<div id="top"></div>
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



<!-- PROJECT LOGO -->
<br />
<div align="center">
<h3 align="center">Raze Munner</h3>

  <p align="center">
    Recursive backtracker maze generator. 
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
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a recursive backtracker maze generator, with solving algorithm based on my own theory which is under development. Read through the theory to find out more about the algorithm:
1. While we create the maze we want to get hold of the information about how the algorithm reached every cell, f.e. it reached the cell on coordinates (x, y) by going left.

2. Using this information we want the algorithm to analyze every cell in the maze and figure out the available ways of getting out of every cell so that the algorithm knows whether there's a 'wall' in front of him or not.

3. We already have an information about how we can get out of every cell, the algorithm acquired it in step one, so f.e. for a given cell if we got to it by going left, naturally we can get out of it by going right, right? :)

4. But what about any other possible ways of getting out? Well for the algorithm to figure them out we have to know how it reached the cell above, on right, below and on left. Now if the cell above was reached by going up then the algorith knows that there is no wall, same for the cell on right which if reached by going right can be accessed by going right and so on for the other cells.

5. Now when we know every cell's ways out, we must eliminate dead ends which are cells that only have a one way of getting out.

6. Then we have to know the location of every cell which has 3 or more ways out of it, these are some sort of crossroads and every road has to be visited by the algorithm.

7. The goal for the algorithm is to move from one crossroad to another and eventually eliminate all of the roads that lead the algorithm to the dead ends resulting in finding a shortest way to solve the maze.

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [Python](https://www.python.org/)
* [PyGame](https://www.pygame.org/news)
* [PyCharm](https://www.jetbrains.com/pycharm/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

1. Install all requirements
2. Run the main.py file

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Pygame
  ```sh
  python -m pip install pygame
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mrowkamaksymilian/raze-munner.git
   ```
   
<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Try with manipulating values of a maze's cell in order to change the maze's size.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Your Name - [LinkedIn](https://www.linkedin.com/in/maksymilian-mr%C3%B3wka/) - mrowkamaksymilian@gmail.com

Project Link: [https://github.com/mrowkamaksymilian/raze-munner](https://github.com/mrowkamaksymilian/raze-munner)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
