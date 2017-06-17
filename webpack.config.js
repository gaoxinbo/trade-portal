var path = require('path');
var HtmlWebpackPlugin = require('html-webpack-plugin');
var CleanWebpackPlugin = require('clean-webpack-plugin')


module.exports = {
  context: path.resolve('./src'),
  entry: { 
    index : './js/index.js',
  },
  output: {
    filename: './static/js/[name].bundle.js',
    path: path.resolve(__dirname, 'dist'),
    publicPath : ""
  },
  plugins: [
      new CleanWebpackPlugin("dist"),
      new HtmlWebpackPlugin({
         "filename": "./index.html",
         "template": "index.html"
        })
  ],

  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      },
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: /node_modules/
      },
    ]
  }

};
