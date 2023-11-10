<script setup lang="ts">
import {
  ClientOnly,
  useRouteLocale,
  useSiteLocaleData,
  withBase,
} from '@vuepress/client'
import { computed, h, onMounted, ref } from 'vue'
import type { FunctionalComponent } from 'vue'
import { useDarkMode, useThemeLocaleData } from '@vuepress/theme-default/lib/client/composables'
import { useRouter } from "vue-router"

const routeLocale = useRouteLocale()
const siteLocale = useSiteLocaleData()
const themeLocale = useThemeLocaleData()
const isDarkMode = useDarkMode()

const navbarBrandObj = {
  "zh": {
    "6th": "第六期",
    "5th": "第五期",
    "other": "其他资料",
    "study": "学习讲义"
  },
  "en": {
    "6th": "The 6th",
    "5th": "The 5th",
    "other": "Other Materials",
    "study": "Study Handouts"
  }
}

let navbarBrandObjCurr = navbarBrandObj["zh"];
let navbarBrandTitleBegin = ref(navbarBrandObjCurr["6th"]);
let navbarBrandTitleEnd = ref(navbarBrandObjCurr["study"]);

onMounted(() => {
    const router = useRouter();
    router.beforeEach((to) => {
        const path = to.path;
        if (path.indexOf("/en/") != -1) {
          navbarBrandObjCurr = navbarBrandObj["en"]
        }
        else {
          navbarBrandObjCurr = navbarBrandObj["zh"]
        }

        if (path.indexOf("ics-pa") != -1) {
          navbarBrandTitleBegin.value = "";
          navbarBrandTitleEnd.value = navbarBrandObjCurr["other"];
        }
        else if (path.indexOf("2306") != -1 || path === "/" || path === "/en/") {
          navbarBrandTitleBegin.value = navbarBrandObjCurr["6th"];
          navbarBrandTitleEnd.value = navbarBrandObjCurr["study"];
        }
        else if (path.indexOf("2205") != -1) {
          navbarBrandTitleBegin.value = navbarBrandObjCurr["5th"];
          navbarBrandTitleEnd.value = navbarBrandObjCurr["study"];
        }
    });
});

const navbarBrandLink = computed(
  () => themeLocale.value.home || routeLocale.value
)
const navbarBrandTitle = computed(() => siteLocale.value.title)
const navbarBrandLogo = computed(() => {
  if (isDarkMode.value && themeLocale.value.logoDark !== undefined) {
    return themeLocale.value.logoDark
  }
  return themeLocale.value.logo
})
const NavbarBrandLogo: FunctionalComponent = () => {
  if (!navbarBrandLogo.value) return null
  const img = h('img', {
    class: 'logo',
    src: withBase(navbarBrandLogo.value),
    alt: navbarBrandTitle.value,
  })
  if (themeLocale.value.logoDark === undefined) {
    return img
  }
  // wrap brand logo with <ClientOnly> to avoid ssr-mismatch
  // when using a different brand logo in dark mode
  return h(ClientOnly, () => img)
}
</script>

<template>
  <div>
  <!-- <RouterLink :to="navbarBrandLink"> -->
    <span
      v-if="navbarBrandTitle"
      class="site-name"
      :class="{ 'can-hide': navbarBrandLogo }"
    >
      <!-- {{ navbarBrandTitle }} -->
      {{ navbarBrandTitleBegin }}
    </span>

    <NavbarBrandLogo style="margin-right:0px; position:relative; top:1px;" />

    <span
      v-if="navbarBrandTitle"
      class="site-name"
      :class="{ 'can-hide': navbarBrandLogo }"
    >
      <!-- {{ navbarBrandTitle }} -->
      {{ navbarBrandTitleEnd }}
    </span>
  <!-- </RouterLink> -->
  </div>
</template>
