#!/usr/bin/env python3
"""风险等级描述，与 效果验证/维度得分描述.xlsx 同步。"""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
SCORE_XLSX = ROOT / "效果验证" / "维度得分描述.xlsx"

# 内置备份（xlsx 缺失时使用）
SCORE_DESCRIPTIONS = {
    ("抑郁悲观", "低"): "情绪偶有低落，注意力基本稳定，做事投入正常",
    ("抑郁悲观", "中"): "情绪时常低落，注意力容易分散，做事投入不足",
    ("抑郁悲观", "高"): "情绪长期低落，注意力难集中，做事明显没劲",
    ("焦虑不安", "低"): "平时较少多想，心里基本踏实，确认后很少再问",
    ("焦虑不安", "中"): "遇事容易挂心，心里不太踏实，确认后还会再问",
    ("焦虑不安", "高"): "经常放心不下，心里很难踏实，确认多次仍不安心",
    ("冲动违规", "低"): "基本能守规矩，很少与人起冲突，出错后愿意改正",
    ("冲动违规", "中"): "有时不按规矩，容易与人起争执，出错后不太愿改",
    ("冲动违规", "高"): "经常不守规矩，动不动就起冲突，出错后很难改过",
    ("行为古怪", "低"): "说话略显特别，想法和别人差不多，配合基本正常",
    ("行为古怪", "中"): "说话有些难懂，想法有些不同，别人不太愿配合",
    ("行为古怪", "高"): "说话常难听懂，想法比较特别，别人较少愿配合",
    ("偏执多疑", "低"): "很少怀疑别人，不太乱猜用意，合作推进顺利",
    ("偏执多疑", "中"): "有时怀疑别人，容易往坏处想，沟通需要反复",
    ("偏执多疑", "高"): "经常怀疑别人，总觉得被人算计，合作推进费劲",
    ("喜怒无常", "低"): "情绪基本稳定，对事反应正常，对人态度平稳",
    ("喜怒无常", "中"): "情绪起伏明显，对事反应偏大，对人忽冷忽热",
    ("喜怒无常", "高"): "情绪变化很快，对事反应激烈，对人态度反差大",
    ("刻板固执", "低"): "新做法能跟上，事情敢交人，做事效率基本正常",
    ("刻板固执", "中"): "新做法跟得较慢，事情不太放手，反复检查影响效率",
    ("刻板固执", "高"): "新做法很难适应，事情基本不放手，经常重复返工",
    ("妄想离奇", "低"): "能分清现实想法，做事判断正常，用工风险基本可控",
    ("妄想离奇", "中"): "有时分不清现实和猜想，做事判断偶有偏差，用工需留意",
    ("妄想离奇", "高"): "常分不清现实和幻想，做事判断容易出错，用工风险较高",
}


def get_description(dimension: str, level: str) -> str:
    return SCORE_DESCRIPTIONS.get((dimension, level), "")


def load_from_xlsx() -> dict[tuple[str, str], str]:
    """从 xlsx 读取；失败则返回内置表。"""
    if not SCORE_XLSX.exists():
        return dict(SCORE_DESCRIPTIONS)
    try:
        import openpyxl

        wb = openpyxl.load_workbook(SCORE_XLSX, read_only=True, data_only=True)
        ws = wb.active
        out = {}
        for row in ws.iter_rows(min_row=2, values_only=True):
            if row and row[0] and row[1] and row[2]:
                out[(str(row[0]).strip(), str(row[1]).strip())] = str(row[2]).strip()
        wb.close()
        return out if out else dict(SCORE_DESCRIPTIONS)
    except Exception:
        return dict(SCORE_DESCRIPTIONS)
