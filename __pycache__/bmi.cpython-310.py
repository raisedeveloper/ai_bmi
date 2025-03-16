o
    }��g  �                   @   s   G d d� d�Z dS )c                   @   s,   e Zd Zdd� Zdd� Zdd� Zdd� Zd	S )
�BMICalculatorc                 C   s   || _ |d | _dS )uo   
        BMI 계산기 초기화
        :param weight: 체중 (kg)
        :param height: 신장 (cm)
        �d   N��weight�height)�selfr   r   � r   �"C:\aiproject\classExample02\bmi.py�__init__   s   zBMICalculator.__init__c                 C   s   | j | jd  S )u$   BMI 계산: 체중(kg) / 신장^2(m)�   r   )r   r   r   r   �calculate_bmi   s   zBMICalculator.calculate_bmic                 C   s<   | � � }|dk r
dS |dk rdS |dk rdS |dk rdS d	S )
u   BMI 범주 반환g     �2@u	   저체중�   u   정상�   u	   과체중�   u   비만u   고도비만)r   )r   �bmir   r   r   �get_bmi_category   s   zBMICalculator.get_bmi_categoryc                 C   s    | � � }| �� }t|d�|d�S )u   BMI 결과 반환r
   )r   �category)r   r   �round)r   r   r   r   r   r   �
get_result   s
   �zBMICalculator.get_resultN)�__name__�
__module__�__qualname__r	   r   r   r   r   r   r   r   r      s
    	r   N)r   r   r   r   r   �<module>   s    