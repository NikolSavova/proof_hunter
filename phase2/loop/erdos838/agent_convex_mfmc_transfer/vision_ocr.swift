import AppKit
import Foundation
import Vision

guard CommandLine.arguments.count >= 2 else {
    fputs("usage: vision_ocr image...\n", stderr)
    exit(2)
}

for path in CommandLine.arguments.dropFirst() {
    guard let image = NSImage(contentsOfFile: path),
          let data = image.tiffRepresentation,
          let bitmap = NSBitmapImageRep(data: data),
          let cgImage = bitmap.cgImage else {
        fputs("cannot read \(path)\n", stderr)
        continue
    }

    let request = VNRecognizeTextRequest()
    request.recognitionLevel = .accurate
    request.usesLanguageCorrection = true
    request.recognitionLanguages = ["ja-JP", "en-US"]
    let handler = VNImageRequestHandler(cgImage: cgImage, options: [:])
    try handler.perform([request])

    print("===== \(path) =====")
    let observations = (request.results ?? []).sorted {
        if abs($0.boundingBox.maxY - $1.boundingBox.maxY) > 0.008 {
            return $0.boundingBox.maxY > $1.boundingBox.maxY
        }
        return $0.boundingBox.minX < $1.boundingBox.minX
    }
    for observation in observations {
        if let candidate = observation.topCandidates(1).first {
            print(candidate.string)
        }
    }
}
