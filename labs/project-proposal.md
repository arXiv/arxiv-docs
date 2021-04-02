{% macro pendo() %}
<script>
(function(apiKey){
    (function(p,e,n,d,o){var v,w,x,y,z;o=p[d]=p[d]||{};o._q=[];
    v=['initialize','identify','updateOptions','pageLoad','track'];for(w=0,x=v.length;w<x;++w)(function(m){
        o[m]=o[m]||function(){o._q[m===v[0]?'unshift':'push']([m].concat([].slice.call(arguments,0)));};})(v[w]);
        y=e.createElement(n);y.async=!0;y.src='https://content.analytics.arxiv.org/agent/static/'+apiKey+'/pendo.js';
        z=e.getElementsByTagName(n)[0];z.parentNode.insertBefore(y,z);})(window,document,'script','pendo');

        // Call this whenever information about your visitors becomes available
        // Please use Strings, Numbers, or Bools for value types.
        pendo.initialize({
            visitor: {
                id:              'arxiv-labs-user'   // Required if user is logged in
                // email:        // Recommended if using Pendo Feedback, or NPS Email
                // full_name:    // Recommended if using Pendo Feedback
                // role:         // Optional
                // You can add any additional visitor level key-values here,
                // as long as it's not one of the above reserved names.
            },

            account: {
                id:           'ARXIV-LABS' // Highly recommended
                // name:         // Optional
                // is_paying:    // Recommended if using Pendo Feedback
                // monthly_value:// Recommended if using Pendo Feedback
                // planLevel:    // Optional
                // planPrice:    // Optional
                // creationDate: // Optional
                // You can add any additional account level key-values here,
                // as long as it's not one of the above reserved names.
            }
        });
})('d6494389-b427-4103-7c76-03182ecc8e60');
</script>
{% endmacro %}
{{ pendo() }}
# Submit your project to arXivLabs

<style>
.mkd-img-right {
  float:right;
  width:100%;
  margin-top:0;
}
.mkd-img-thumb {
  max-width:150px !important;
}
blockquote {
  border-left:0;
  margin:0;
  padding:0;
}
.form-proposals {
  margin-bottom: 2em;
  padding-top: 2em;
  border: 2px solid #;
  border-radius: 1em;
  -webkit-box-shadow: 1px 1px 2px 1px rgba(116,144,153,0.76);
  box-shadow: 1px 1px 2px 1px rgba(116,144,153,0.76);
}
@media (min-width: 576px) {
  .mkd-img-right {
    width:calc(50% - 1.25em);
    margin-left:2em;
  }
}
</style>
<img alt="arXivLabs logo" src="images/smileybones-labs-icon.png" class="mkd-img-right mkd-img-thumb"/>

arXiv welcomes anyone, from single individuals to large companies, to contribute ideas and propose their project for arXivLabs. All projects must abide by arXiv’s values of openness, community, excellence, and user data privacy. Learn more about arXiv's [Labs criteria](criteria) and [API data usage](https://arxiv.org/help/api/).

To propose a project fill out all fields in our project proposal form. Scroll within the frame below and fill out all fields on each page (total of four steps).

<iframe src="https://cornell.ca1.qualtrics.com/jfe/form/SV_6utTdLVDVlaTz5Y" height="650px" width="100%" class="form-proposals"></iframe>

-Is the form above not displaying? <a href="https://cornell.ca1.qualtrics.com/jfe/form/SV_6utTdLVDVlaTz5Y">Open it in Qualtrics</a>-
