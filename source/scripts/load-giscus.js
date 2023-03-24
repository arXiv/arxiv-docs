document.addEventListener('DOMContentLoaded', function () {
    const giscusAttributes = {
      "src": "https://giscus.app/client.js",
      "data-repo": "arxiv/discussion",
      "data-repo-id": "R_kgDOHzoccw",
      "data-category-id": "DIC_kwDOHzocc84CQwr5",
      "data-mapping": "pathname",
      "data-strict": "0",
      "data-reactions-enabled": "1",
      "data-emit-metadata": "0",
      "data-input-position": "bottom",
      "data-lang": "en",
      "data-theme": "https://github.com/arXiv/discussion/tree/master/docs/stylesheets/arxiv-giscus-theme.css",
      "crossorigin": "use-credentials",
      "async": "",
  };

  // Dynamically create script tag
  const giscusScript = document.createElement("script");
  Object.entries(giscusAttributes).forEach(([key, value]) => giscusScript.setAttribute(key, value));
  document.getElementsByTagName("article")[0].appendChild(giscusScript);
})