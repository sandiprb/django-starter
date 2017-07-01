module.exports = {
	plugins: [
	require('postcss-import'),
	require('postcss-mixins'),
	require('postcss-simple-vars'),
	require('postcss-color-function'),
	require('postcss-nested'),
	require('postcss-extend'),
	require('postcss-discard-comments'),
	require('postcss-discard-empty'),
	require('autoprefixer')({
    	'browsers': '> 1%, IE 6, Explorer >= 10, Safari >= 7'
    })
	]
}
