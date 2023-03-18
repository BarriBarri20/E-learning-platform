import React, { Component } from 'react';
import { render } from 'react-dom';

export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <div>
                <h1>Hello </h1>
                <p>Start editing to see some magic happen : </p>
            </div>
        );
    }
}

const appDiv = document.getElementById('app');

render(<App />, appDiv);