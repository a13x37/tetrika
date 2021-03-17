from flask import Flask, request, jsonify


def appearance(intervals):
    lesson_start = intervals['lesson'][0]
    lesson_end = intervals['lesson'][1]

    def chunk(list):
        new_list = []
        for i in range(0, len(list), 2):
            new_list.append([list[i], list[i+1]])
        return new_list

    chunked_pupil = chunk(intervals['pupil'])
    chunked_tutor = chunk(intervals['tutor'])

    def intersection(pupil, tutor):
        intersection = []
        for i in pupil:
            pupil_start, pupil_end = i[0], i[1]
            for k in tutor:
                tutor_start, tutor_end = k[0], k[1]
                latest_start = max(pupil_start, tutor_start, lesson_start)
                earlies_end = min(pupil_end, tutor_end, lesson_end)
                if latest_start <= earlies_end:
                    intersection.append([latest_start, earlies_end])
        return intersection

    overall_intersection = intersection(chunked_pupil, chunked_tutor)
    overall_time = 0
    for i in overall_intersection:
        time = i[1] - i[0]
        overall_time += time
    return overall_time


app = Flask(__name__)


@app.route('/', methods=['POST'])
def json_intervals():
    result = appearance(request.json)
    return jsonify(result)
