<template>
	<view>
		<cu-custom bgImage="../../static/img/sylb2244.jpg" :isBack="true">
			<block slot="backText">返回</block>
			<block slot="content">{{fullname}}</block>
		</cu-custom>
		<view class="cu-bar bg-white solid-bottom margin-top">
			<view class="action">
				<text class="cuIcon-title text-blue"></text>{{ChapterSN}}
			</view>
		</view>
		<scroll-view class="padding bg-white" scroll-y scroll-with-animation :scroll-into-view="'main-'+nowversesn" style="height:calc(100vh - 250upx)" >
			<view class="text-left padding" v-for="(item,index) in contentlist" :key="index" :id="'main-'+item.VerseSN" :class="nowversesn==item.VerseSN?'text-orange':''">
				<view class='cu-tag round' >{{item.VerseSN}}</view>
				{{item.Lection}}
			</view>
		</scroll-view>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				nowversesn:'0',
				booksn:1,
				versesn:1,
				chaptersn:1,
				contentlist:{},
				fullname:'',
				ChapterSN:'',
				loading:false
			}
		},
		onLoad(o) {
			this.booksn = o.booksn;
			this.chaptersn = o.chaptersn;
			this.versesn = o.versesn;
			this.getcontents(o.booksn,o.chaptersn);
		},	
		updated(){
			//凡是数据渲染后再做dom处理的 需要放在updated里
			this.nowversesn=uni.getStorageSync("versesn");
		},
		methods: {
			getcontents(booksn,chaptersn){
				// 获取经文内容
				this.loading = true
				this.$api.getcontents(booksn,chaptersn,{noncestr: Date.now()}).then((res)=>{
					this.loading = false;
					this.contentlist = res.data;
					this.ChapterSN=res.data[0]['ChapterSN']
					this.fullname=res.data[0]['VolumeSN'].FullName;
				}).catch((err)=>{
					this.loading = false;
					console.log('request fail', err);
				});
			}
		}
	}
</script>

<style>

</style>
