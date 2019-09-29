const path = require('path');
const webpack = require('webpack');

module.exports = {
	plugins: [
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
    ],
    entry: {
        'app': [
            path.join(__dirname, '/client/index.js'),
        ],
    },
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'static/'),
    },
    module: {
        rules: [
            {
                test:  /\.jsx?$/,
                exclude: /node_modules/,
                loader: ['babel-loader']
            },
            {
                test: /\.(png|jpg|jpeg)(\?v=\d+\.\d+\.\d+)?$/,
                use: [
                  {
                    loader: 'file-loader',
                    options: {
                      name: '[name].[ext]',
                      outputPath: path.resolve(__dirname, 'static/images/'),
                    }
                  }
                ]
            },
            {
                test: /\.s[ac]ss$/i,
                exclude: /node_modules/,
                use: [
                  // Creates `style` nodes from JS strings
                  'style-loader',
                  // Translates CSS into CommonJS
                  'css-loader',
                  // Compiles Sass to CSS
                  'sass-loader',
                ],
            },
        ]
    },
    resolve: {
        extensions: ['.js', '.jsx', '.scss']
    },
    devtool: 'source-map',
}
