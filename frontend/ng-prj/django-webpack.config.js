const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    plugins:[
        new BundleTracker({filename: '../../backend/prj/static/webpack-stats-angular.json'})
    ],
    output: {
        path: require('path').resolve('../../backend/prj/static/angular'),
        filename: "[name]-[hash].js"
    }
};