<template>
    <div class="container">
        <h1>Lista de Elementos</h1>

        
        <b-card
            :title = 'element.title'
            
        >
            <b-card-text>
            {{ element.description }}
            </b-card-text>

            <b-button href="#" variant="primary">Go somewhere</b-button>
        </b-card>
        
        
    </div>
</template>

<script>
export default {

    created: function(){
        this.findOne();
    },

    data() {
        return {
            element : Object
        };
    },
    methods: {
        findOne: function(){
            
            fetch('http://127.0.0.1:8000/api/element/' + this.$route.params.id + '/?format=json')
            .then(res => res.json() )
            .then(res => this.element = res);
        },
        
    },
}
</script>

<style>

    .box{
        border: 1px solid #ccc;
        margin-bottom:5px;
    }
    
</style>