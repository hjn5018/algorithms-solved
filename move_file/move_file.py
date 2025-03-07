import os
import re
import shutil

def organize_files(source_folder):
    # 플랫폼 목록
    platforms = ['hackerrank', 'leetcode', 'acmicpc', 'programmers']
    
    # 각 플랫폼별 폴더 생성
    for platform in platforms:
        platform_folder = os.path.join(source_folder, platform)
        if not os.path.exists(platform_folder):
            os.makedirs(platform_folder)
            print(f"폴더 생성: {platform_folder}")
    
    # 파일 목록 가져오기
    files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # 각 파일에 대해 플랫폼 확인 및 이동
    for file in files:
        file_path = os.path.join(source_folder, file)
        target_platform = identify_platform(file_path, platforms)
        
        if target_platform:
            target_folder = os.path.join(source_folder, target_platform)
            target_path = os.path.join(target_folder, file)
            
            # 파일 이동
            shutil.move(file_path, target_path)
            print(f"파일 이동: {file} -> {target_platform} 폴더")
        else:
            print(f"플랫폼을 식별할 수 없음: {file}")

def identify_platform(file_path, platforms):
    # 파일명에서 플랫폼 확인
    file_name = os.path.basename(file_path)
    for platform in platforms:
        if platform.lower() in file_name.lower():
            return platform
    
    # 파일 내용에서 플랫폼 확인
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            for platform in platforms:
                if platform.lower() in content.lower():
                    return platform
    except Exception as e:
        print(f"파일 읽기 오류 ({file_path}): {e}")
    
    return None

if __name__ == "__main__":
    # Windows 경로 형식으로 설정
    source_folder = r'C:\Users\hjn50\Desktop\python_yeonsuep\nbc_ai_track_sql'
    organize_files(source_folder)
    print("파일 분류 완료!")