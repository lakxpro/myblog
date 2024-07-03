const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  entry: {
    app: './static/src/js/index.js',
    styles: './static/src/scss/main.scss'
  },
  output: {
    filename: '[name].js',
    path: path.resolve(__dirname, 'static/dist'),
    publicPath: '/static/dist/',
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: 'babel-loader',
      },
      {
        test: /\.css$/i,
        use: [MiniCssExtractPlugin.loader, 'css-loader'],
      },
      {
        test: /\.(scss)$/,
        use: [
          MiniCssExtractPlugin.loader, // Extract CSS into files
          'css-loader', // translates CSS into CommonJS modules
          {
            loader: 'postcss-loader', // Run postcss actions
            options: {
              postcssOptions: {
                plugins: () => [
                  require('autoprefixer'),
                ],
              },
            },
          },
          'sass-loader' // compiles Sass to CSS
        ],
      },
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: '[name].css',
    }),
    new BundleTracker({filename: 'webpack-stats.json'}),
  ],
  mode: 'development',
  devServer: {
    static: path.join(__dirname, 'static/dist'),
    hot: true,
    port: 3000,
  },
};
