const NavbarTemplate = document.createElement('template');
NavbarTemplate.innerHTML = `

<style>
.navbar {
    background-color: white;
}

.navbar ul {
    margin: 0;
    padding-top: 10px;
    overflow: auto;
}

.navbar li {
    padding-top: 7px;
    margin: 10px 5px;
    list-style: none;
    float: left;
}

.navbar li a {
    text-decoration: none;
    padding: 3px 10px;
    color: black;
}

#title1 {
    font-size: 25px;
    padding: 3px;
    padding-left: 100px;
    padding-right: 0;
    margin-right: 0;
    font-weight: bold;
    color: black;
}

#title2 {
    font-size: 25px;
    font-weight: bold;
    padding: 3px;
    padding-right: 150px;
    padding-left: 0;
    margin-left: 0;
    color: mediumspringgreen;
}
</style>


<nav class="navbar">
<ul>
    <li id="title1">MEDI</li>
    <li id="title2">HEALTH</li>
    <li><a href="edi.html">HOME</a></li>
    <li><a href="chestedi.html">EXERCISE</a></li>
    <li><a href="ddf.html">DISEASE DIAGNOSE</a></li>
    <li><a href="nutrition.html">NUTRITION</a></li>
    <li><a href="../meditation/index.html">MEDITATION</a></li>
</ul>
</nav>

`

class Navbar extends HTMLElement {
    constructor() {
        // Always call super first in constructor
        super();
    }

    connectedCallback() {
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.appendChild(NavbarTemplate.content);
    }
}

customElements.define('nav-comp', Navbar);