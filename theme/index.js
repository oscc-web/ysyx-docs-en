/* eslint-disable capitalized-comments */
const
	{ defaultTheme } = require('@vuepress/theme-default'),
	{ path } = require('@vuepress/utils'),
	custom = name => path.resolve(__dirname, `components/${name}.vue`)
module.exports = options => ({
	name: 'vuepress-theme-local',
	extends: defaultTheme(options),
	// layouts: {
	// 	Layout: path.resolve(__dirname, 'layouts/Layout.vue'),
	// },
	alias: {
		'@theme/ToggleColorModeButton.vue': custom('ThemeSwitch'),
		'@theme/NavbarBrand.vue': custom('NavbarBrand'),
		'@theme/NavbarItems.vue': custom('NavbarItems')
	}
})
