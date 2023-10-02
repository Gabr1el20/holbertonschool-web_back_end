import getResponseFromAPI from './0-promise';

const response = getResponseFromAPI();
/* eslint-disable */
console.log(response instanceof Promise);
