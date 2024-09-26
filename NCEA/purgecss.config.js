// delete this before submitting!!! ⚠️⚠️⚠️
module.exports = {
    content: [
      './templates/**/*.html',  
      './static/js/**/*.js',   
    ],
    css: ['./static/styles/tailwind.min.css'], 
    output: './static/styles/global-purged.css', 
    defaultExtractor: content => content.match(/[\w-/:]+(?<!:)/g) || [],
    safelist: [],  
  }
  
 // purgecss --config ./purgecss.config.js
