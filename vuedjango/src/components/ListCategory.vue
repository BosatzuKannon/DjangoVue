<template>
    <div class="container">
        <h1>Lista de Elementos</h1>
        
        <div class="box" v-for="e in elements" v-bind:key="e.id"> 
            <router-link :to=" '/detail/' + e.id">
                <b-card
                    :title = 'e.title'
                    
                >
                    <b-card-text>
                    {{ e.description }}
                    </b-card-text>

                    <b-button href="#" variant="primary">Go somewhere</b-button>
                </b-card>
            </router-link>
        </div>
        
    </div>
</template>

<script>
export default {

    created: function(){
        this.findAll()
    },

    data() {
        return {
            elements : []
        };
    },
    methods: {
        findAll: function(){
            
            fetch('http://127.0.0.1:8000/api/element/?format=json')
            .then(res => res.json() )
            .then(res => this.elements = res)
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