const path = require('path')

module.exports = {
    entry: './static/user/index.js',
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, "static", "user")
    },
    resolve: {
        extensions: ['.ts', '...'],
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [
                    'style-loader',
                    'css-loade'
                ]
            },
            {
                test: /\.tsx?$/,
                use: 'ts-loader',
            }
        ]
    }
}