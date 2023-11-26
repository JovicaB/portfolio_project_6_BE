import heapq

from data.data import PI1_FACTOR_NAMES, PI1_WORK_CONDITIONS_IMPROVEMENT_DATA
from data.data import PI2_QUESTIONS, PI2_INTERPRETATION_COLUMNS, PI2_SHORT_INTERPRETATION, PI2_PERSONALITIES_INTERPRETATION
from data.data import PI3_INTERPRETATION_COLUMNS


class P1Interpretation:
    """
    A class for structuring and display of pi_1 assesment and interpretation data
    """

    def __init__(self, data) -> None:
        self.data = data

    def average_results(self):
        """
        returns average results for each job satisfaction factor [list of 20 averages]
        """
        data = [result[0] for result in self.data]
        averages = [round(sum(values) / len(values), 2)
                    for values in zip(*data)]
        return averages

    def descriptive_results(self):
        """
        returns job satisfaction improvement results from user [list of user suggestions]
        """
        result = [result[1] for result in self.data]
        return result

    def result_interpretation(self):
        """
        count, max value, min value, data for interpretation page
        """

        data_count = len(self.data)
        averages = self.average_results()
        factors = PI1_FACTOR_NAMES

        max_values = heapq.nlargest(3, enumerate(averages), key=lambda x: x[1])
        max_factors = [(factors[index], value) for index, value in max_values]

        min_values = heapq.nsmallest(
            3, enumerate(averages), key=lambda x: x[1])
        min_factors = [(factors[index], value) for index, value in min_values]

        int_results = {
            'count results': data_count,
            'max score': max_factors,
            'min score': min_factors
        }

        return int_results

    def satisfaction_improvement_data(self):
        """
        returns improvement [list] data for 3 job satifaction factors with lowest score
        """
        min_results = [data[0]
                       for data in self.result_interpretation()['min score']]
        pp1_improvement_data = {
            data: PI1_WORK_CONDITIONS_IMPROVEMENT_DATA[data] for data in min_results}
        return pp1_improvement_data


class PI2Questionnaire:
    """
    A class with the question_answer method for returning question and answer based on counter value
    """
    @staticmethod
    def question_answer(counter: int):
        return {'Q': PI2_QUESTIONS[counter][0], 'A': PI2_QUESTIONS[counter][1], 'B': PI2_QUESTIONS[counter][2]}


class PI2MBTIType:
    """
    A class for MBTI profile type calculation based on provided test answers
    """

    def __init__(self, data) -> None:
        self.data = data

    def mbti_dimension_count(self, mbti_dimension: str):
        """
        counts number of answers in a result dictionary using input_map; 
        data example = ["A", "A", "B"...]
        """
        input_map = PI2_INTERPRETATION_COLUMNS
        score = 0

        for i in input_map[mbti_dimension]:
            if self.data[i - 1] == 'A':
                score += 1
        return score

    def mbti_type(self):
        """
        calculates personality type
        """
        mbti_profile = ''

        dim_E = self.mbti_dimension_count('EI')
        dim_I = 10 - dim_E
        if dim_E < dim_I:
            mbti_profile = mbti_profile + 'I'
        else:
            mbti_profile = mbti_profile + 'E'

        dim_S = self.mbti_dimension_count('SN')
        dim_N = 20 - dim_S
        if dim_S < dim_N:
            mbti_profile = mbti_profile + 'N'
        else:
            mbti_profile = mbti_profile + 'S'

        dim_T = self.mbti_dimension_count('TF')
        dim_F = 20 - dim_T
        if dim_T < dim_F:
            mbti_profile = mbti_profile + 'F'
        else:
            mbti_profile = mbti_profile + 'T'

        dim_J = self.mbti_dimension_count('JP')
        dim_P = 20 - dim_J
        if dim_J < dim_P:
            mbti_profile = mbti_profile + 'P'
        else:
            mbti_profile = mbti_profile + 'J'

        return mbti_profile


class P2Interpretation:
    """
    A class for structuring pi_2 interpretation data
    """

    def __init__(self, mbti_type: str) -> None:
        self.mbti_type = mbti_type

    def short_interpretation(self):
        result = [value for value in PI2_SHORT_INTERPRETATION.values()
                  if value['MBTI_code'] == self.mbti_type]
        return result

    def detailed_interpretation(self):
        result = [value for key, value in PI2_PERSONALITIES_INTERPRETATION.items(
        ) if key == self.mbti_type]
        return result


class P3Interpretation:
    """
    A class for structuring and display of pi_3 interpretation data
    """

    def __init__(self, data) -> None:
        self.data = data

    def PCLR_score(self, factor):
        score = 0
        for i in PI3_INTERPRETATION_COLUMNS[factor]:
            score += self.data[i - 1]
        return score

    def PCLR_results(self):
        primary_result = self.PCLR_score('PCR_TOT')
        secondary_result = [self.PCLR_score(
            'PCR_DET'), self.PCLR_score('PCR_ANT')]
        result = [[primary_result, secondary_result]]
        return result
