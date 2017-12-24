#!/usr/bin/env python
# encoding: utf-8

row_data = [
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'python',
                        'name': 'Python语言'
                    },
                    {
                        'code': 'c',
                        'name': 'C语言'
                    },
                    {
                        'code': 'java',
                        'name': 'Java语言'
                    },
                    {
                        'code': 'javascript',
                        'name': 'JavaScript'
                    }
                ],
                'code': 'bcyy',
                'name': '编程语言'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'jsjwl',
                        'name': '计算机网络'
                    },
                    {
                        'code': 'czxt',
                        'name': '操作系统'
                    },
                    {
                        'code': 'sjjg',
                        'name': '数据结构'
                    },
                    {
                        'code': 'jsjzcyl',
                        'name': '计算机组成原理'
                    }
                ],
                'code': 'cxsj',
                'name': '程序设计'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'wlaq',
                        'name': '网络安全'
                    },
                    {
                        'code': 'nxpj',
                        'name': '逆向破解'
                    }
                ],
                'code': 'xxaq',
                'name': '信息安全'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'mjkf',
                        'name': '敏捷开发'
                    },
                    {
                        'code': 'jy',
                        'name': '精益'
                    },
                    {
                        'code': 'xmgl',
                        'name': '项目管理'
                    },
                    {
                        'code': 'cxjf',
                        'name': '持续交付'
                    }
                ],
                'code': 'rjgc',
                'name': '软件工程'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yxkf',
                'name': '游戏开发'
            },
            {
                'sub_categorys': [

                ],
                'code': 'dsj',
                'name': '大数据'
            },
            {
                'sub_categorys': [

                ],
                'code': 'yjs',
                'name': '云计算'
            },
            {
                'sub_categorys': [

                ],
                'code': 'xtjg',
                'name': '系统架构'
            }
        ],
        'code': 'jsj',
        'name': '计算机'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': 'stock',
                        'name': '股票'
                    },
                    {
                        'code': 'insurance',
                        'name': '保险'
                    },
                    {
                        'code': 'bank',
                        'name': '银行'
                    }
                ],
                'code': 'tzlc',
                'name': '投资理财'
            },
            {
                'sub_categorys': [

                ],
                'code': 'qygl',
                'name': '企业管理'
            },
            {
                'sub_categorys': [

                ],
                'code': 'hgjjx',
                'name': '宏观经济学'
            },
            {
                'sub_categorys': [

                ],
                'code': 'wgjjx',
                'name': '微观经济学'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'qtpp',
                        'name': '其他品牌'
                    },
                    {
                        'code': 'hj',
                        'name': '黄酒'
                    },
                    {
                        'code': 'ysj',
                        'name': '养生酒'
                    }
                ],
                'code': 'kjsj',
                'name': '会计／审计'
            },
            {
                'sub_categorys': [

                ],
                'code': 'scyx',
                'name': '市场营销'
            },
            {
                'sub_categorys': [
                    {
                        'code': 'bld',
                        'name': '白兰地'
                    },
                    {
                        'code': 'wsj',
                        'name': '威士忌'
                    }
                ],
                'code': 'blockchain',
                'name': '区块链'
            }
        ],
        'code': 'jjgl',
        'name': '经济管理'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '其他食用油',
                        'name': '其他食用油'
                    },
                    {
                        'code': '菜仔油',
                        'name': '菜仔油'
                    },
                    {
                        'code': '花生油',
                        'name': '花生油'
                    },
                    {
                        'code': '橄榄油',
                        'name': '橄榄油'
                    },
                    {
                        'code': '礼盒',
                        'name': '礼盒'
                    }
                ],
                'code': '食用油',
                'name': '食用油'
            },
            {
                'sub_categorys': [
                    {
                        'code': '面粉/面条',
                        'name': '面粉/面条'
                    },
                    {
                        'code': '大米',
                        'name': '大米'
                    },
                    {
                        'code': '意大利面',
                        'name': '意大利面'
                    }
                ],
                'code': '米面杂粮',
                'name': '米面杂粮'
            },
            {
                'sub_categorys': [
                    {
                        'code': '调味油/汁',
                        'name': '调味油/汁'
                    },
                    {
                        'code': '酱油/醋',
                        'name': '酱油/醋'
                    }
                ],
                'code': '厨房调料',
                'name': '厨房调料'
            },
            {
                'sub_categorys': [

                ],
                'code': '南北干货',
                'name': '南北干货'
            },
            {
                'sub_categorys': [

                ],
                'code': '方便速食',
                'name': '方便速食'
            },
            {
                'sub_categorys': [

                ],
                'code': '调味品',
                'name': '调味品'
            }
        ],
        'code': 'wyxx',
        'name': '外语学习'   # here, don't change sub_cat
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '西红柿',
                        'name': '西红柿'
                    },
                    {
                        'code': '韭菜',
                        'name': '韭菜'
                    },
                    {
                        'code': '青菜',
                        'name': '青菜'
                    }
                ],
                'code': '有机蔬菜',
                'name': '有机蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': '甘蓝',
                        'name': '甘蓝'
                    },
                    {
                        'code': '胡萝卜',
                        'name': '胡萝卜'
                    },
                    {
                        'code': '黄瓜',
                        'name': '黄瓜'
                    }
                ],
                'code': '精选蔬菜',
                'name': '精选蔬菜'
            },
            {
                'sub_categorys': [
                    {
                        'code': '火龙果',
                        'name': '火龙果'
                    },
                    {
                        'code': '菠萝蜜',
                        'name': '菠萝蜜'
                    },
                    {
                        'code': '奇异果',
                        'name': '奇异果'
                    }
                ],
                'code': '进口水果',
                'name': '进口水果'
            },
            {
                'sub_categorys': [
                    {
                        'code': '水果礼盒',
                        'name': '水果礼盒'
                    },
                    {
                        'code': '苹果',
                        'name': '苹果'
                    },
                    {
                        'code': '雪梨',
                        'name': '雪梨'
                    }
                ],
                'code': '国产水果',
                'name': '国产水果'
            }
        ],
        'code': '蔬菜水果',
        'name': '蔬菜水果'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [
                    {
                        'code': '果冻',
                        'name': '果冻'
                    },
                    {
                        'code': '枣类',
                        'name': '枣类'
                    },
                    {
                        'code': '蜜饯',
                        'name': '蜜饯'
                    },
                    {
                        'code': '肉类零食',
                        'name': '肉类零食'
                    },
                    {
                        'code': '坚果炒货',
                        'name': '坚果炒货'
                    }
                ],
                'code': '休闲零食',
                'name': '休闲零食'
            },
            {
                'sub_categorys': [
                    {
                        'code': '创意喜糖',
                        'name': '创意喜糖'
                    },
                    {
                        'code': '口香糖',
                        'name': '口香糖'
                    },
                    {
                        'code': '软糖',
                        'name': '软糖'
                    },
                    {
                        'code': '棒棒糖',
                        'name': '棒棒糖'
                    }
                ],
                'code': '糖果',
                'name': '糖果'
            },
            {
                'sub_categorys': [
                    {
                        'code': '夹心巧克力',
                        'name': '夹心巧克力'
                    },
                    {
                        'code': '白巧克力',
                        'name': '白巧克力'
                    },
                    {
                        'code': '松露巧克力',
                        'name': '松露巧克力'
                    },
                    {
                        'code': '黑巧克力',
                        'name': '黑巧克力'
                    }
                ],
                'code': '巧克力',
                'name': '巧克力'
            },
            {
                'sub_categorys': [
                    {
                        'code': '牛肉干',
                        'name': '牛肉干'
                    },
                    {
                        'code': '猪肉脯',
                        'name': '猪肉脯'
                    },
                    {
                        'code': '牛肉粒',
                        'name': '牛肉粒'
                    },
                    {
                        'code': '猪肉干',
                        'name': '猪肉干'
                    }
                ],
                'code': '肉干肉脯/豆干',
                'name': '肉干肉脯/豆干'
            },
            {
                'sub_categorys': [
                    {
                        'code': '鱿鱼足',
                        'name': '鱿鱼足'
                    },
                    {
                        'code': '鱿鱼丝',
                        'name': '鱿鱼丝'
                    },
                    {
                        'code': '墨鱼/乌贼',
                        'name': '墨鱼/乌贼'
                    },
                    {
                        'code': '鱿鱼仔',
                        'name': '鱿鱼仔'
                    },
                    {
                        'code': '鱿鱼片',
                        'name': '鱿鱼片'
                    }
                ],
                'code': '鱿鱼丝/鱼干',
                'name': '鱿鱼丝/鱼干'
            }
        ],
        'code': '休闲食品',
        'name': '休闲食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '进口奶品',
                'name': '进口奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': '国产奶品',
                'name': '国产奶品'
            },
            {
                'sub_categorys': [

                ],
                'code': '奶粉',
                'name': '奶粉'
            },
            {
                'sub_categorys': [

                ],
                'code': '有机奶',
                'name': '有机奶'
            },
            {
                'sub_categorys': [

                ],
                'code': '原料奶',
                'name': '原料奶'
            }
        ],
        'code': '奶类食品',
        'name': '奶类食品'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '菌菇类',
                'name': '菌菇类'
            },
            {
                'sub_categorys': [

                ],
                'code': '腌干海产',
                'name': '腌干海产'
            },
            {
                'sub_categorys': [

                ],
                'code': '汤料',
                'name': '汤料'
            },
            {
                'sub_categorys': [

                ],
                'code': '豆类',
                'name': '豆类'
            },
            {
                'sub_categorys': [

                ],
                'code': '干菜/菜干',
                'name': '干菜/菜干'
            },
            {
                'sub_categorys': [

                ],
                'code': '干果/果干',
                'name': '干果/果干'
            },
            {
                'sub_categorys': [

                ],
                'code': '豆制品',
                'name': '豆制品'
            },
            {
                'sub_categorys': [

                ],
                'code': '腊味',
                'name': '腊味'
            }
        ],
        'code': '天然干货',
        'name': '天然干货'
    },
    {
        'sub_categorys': [
            {
                'sub_categorys': [

                ],
                'code': '白茶',
                'name': '白茶'
            },
            {
                'sub_categorys': [

                ],
                'code': '红茶',
                'name': '红茶'
            },
            {
                'sub_categorys': [

                ],
                'code': '绿茶',
                'name': '绿茶'
            }
        ],
        'code': 'dzswdzzw',
        'name': '电子商务／电子政务'
    }
]