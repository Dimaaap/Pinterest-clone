const path = require("path")

module.exports = {
    entry: './src/index.js'
    output: {
        filename: "bundle.js",
        path: path.resolve(__dirname, 'core', 'static')
    }
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
};