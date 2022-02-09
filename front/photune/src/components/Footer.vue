<template>
    <b-row class="footer px-5 py-3" align-h="center">
        <Member v-for="member in members" :key="member.name"
            v-bind="member" />
    </b-row>
        
</template>

<script>
import Member from './Member.vue'

export default {
    name: 'Footer',
    components: {
        Member
    },
    data() {
        return {
            members:[
                {name:'コウヘイ', univ:'横国物理M1', msg:'(ほぼ)初開発なので頑張りました！', filename:'Kohei.jpg'},
                {name:'小形', univ:'東大電気系M2', msg:'FPGAやアナログ回路での研究中', filename:'o_trm.jpg'},
                {name:'ウエクサ', univ:'横国島研M2', msg:'生体信号の研究をしています。', filename:'uekusa_icon.jpg'},
                {name:'青山', univ:'東工大材料系M2', msg:'薄膜研究してます！参加できてよかった！', filename:'aoyama_trm.jpg'},
                {name:'どんぐり', univ:'横国物理工学B4', msg:'物性理論の研究してます．', filename:'donguri.png'},
            ]
        }
    },
}
</script>




<style scoped>
.footer {
    background: #323135;
    color: #98969c;
}
</style>