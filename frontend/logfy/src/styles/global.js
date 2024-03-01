import { createGlobalStyle } from 'styled-components'

export default createGlobalStyle`
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500&display=swap')
    
    * {
        margin: 0!important;
        padding: 0;
        outline: 0;
        box-sizing: border-box;
    }
    
    html, body, #root {
        height: 100%;
    }
    
    body {
        margin: 0!important;
        font: 14px 'Roboto', sans-serif;
        background-color: #ecf1f8;
        color: #333;
        -webkit-font-smoothing: antialiased!important;
    }
    
    ul {
        list-style: none;
    }
`